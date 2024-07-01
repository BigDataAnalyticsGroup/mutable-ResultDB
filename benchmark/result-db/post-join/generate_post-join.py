from collections import defaultdict
from pathlib import Path
from typing import Any
import argparse
import glob
import itertools
import json
import os
import re
import stat
import subprocess
import sys

mutable_job_datatypes = {
    'movie_companies': {
        'movie_id': 'INT NOT NULL',
        'note': 'CHAR 208',
    },
    'title': {
        'id': 'INT NOT NULL',
        'title': 'CHAR 334 NOT NULL',
        'production_year': 'INT',
    },
    'movie_info_idx': {
        'info': 'CHAR 10 NOT NULL',
        'movie_id': 'INT NOT NULL'
    },
    'keyword': {
        'id': 'INT NOT NULL',
        'keyword': 'CHAR 74 NOT NULL',
    },
    'name': {
        'id': 'INT NOT NULL',
        'name': 'CHAR 106 NOT NULL',
    },
    'aka_name': {
        'name': 'CHAR 218 NOT NULL',
        'person_id': 'INT NOT NULL',
    },
    'char_name': {
        'id': 'INT NOT NULL',
        'name': 'CHAR 478 NOT NULL',
    },
    'movie_info': {
        'info': 'CHAR 43 NOT NULL',
        'movie_id': 'INT NOT NULL',
    },
    'movie_keyword': {
        'movie_id': 'INT NOT NULL',
        'keyword_id': 'INT NOT NULL',
    },
    'cast_info': {
        'person_id': 'INT NOT NULL',
        'movie_id': 'INT NOT NULL',
        'person_role_id': 'INT',
    }
}

mutable_star_datatypes = {
    'fact': {
        'id': 'INT NOT NULL',
        'fkd1': 'INT NOT NULL',
        'fkd2': 'INT NOT NULL',
        'fkd3': 'INT NOT NULL',
        'fkd4': 'INT NOT NULL',
        'a': 'INT NOT NULL',
        'b': 'CHAR 16 NOT NULL',
    },
    'dim1': {
        'id': 'INT NOT NULL',
        'a': 'INT NOT NULL',
        'b': 'CHAR 16 NOT NULL',
    },
    'dim2': {
        'id': 'INT NOT NULL',
        'a': 'INT NOT NULL',
        'b': 'CHAR 16 NOT NULL',
    },
    'dim3': {
        'id': 'INT NOT NULL',
        'a': 'INT NOT NULL',
        'b': 'CHAR 16 NOT NULL',
    },
    'dim4': {
        'id': 'INT NOT NULL',
        'a': 'INT NOT NULL',
        'b': 'CHAR 16 NOT NULL',
    },
}

# Get the absolute path of the utils/ directory
utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils'))
# Add utils_path to the Python path
sys.path.append(utils_path)

from query_utility import Relation, JoinGraph, shortest_path
import query_definitions as q_def
import postgres_info


def write_to_file(output_dir: str, output_file: str, text: str, mode: str = 'w') -> None:
    with open(f'{output_dir}/{output_file}', mode) as file:
        file.write(text)

def generate_query(join_graph: JoinGraph) -> tuple[str, str, str]:
    # collect projections, relations and filters
    relations: list[Relation] = join_graph.relations
    joins: list[Join] = join_graph.joins
    projections = defaultdict(list) # map relation alias to a list of projection attributes
    filters: list[str] = []
    for r in relations:
        for p in r.projections:
            projections[r.alias].append(p)
        for f in r.filters:
            filters.append(f)

    # generate SELECT clause
    select_clause = 'SELECT'
    num_proj = 0
    for r_alias, projs in projections.items():
        for proj_attr in projs:
            if num_proj != 0:
                select_clause += ','
            select_clause += f' {r_alias}.{proj_attr}'
            num_proj += 1

    # generate FROM clause
    from_clause = ' FROM'
    for idx, r in enumerate(relations):
        if idx != 0:
            from_clause += ','
        from_clause += f' {r.name} AS {r.alias}'

    # generate WHERE clause
    ## joins
    where_clause = ''
    if joins:
        where_clause += ' WHERE'
    for idx, join in enumerate(joins):
        for lhs_attr, rhs_attr in zip(join.left_attributes, join.right_attributes):
            join_predicate = f'{join.left_relation.alias}.{lhs_attr} = {join.right_relation.alias}.{rhs_attr}'
            where_clause += f' {join_predicate}'
            if idx != len(joins) - 1: # do NOT emit `AND` for last join predicate
                where_clause += ' AND'

    where_clause += ';'

    return select_clause, from_clause, where_clause

def create_injected_cardinalities(query_name: str, join_graph: JoinGraph, config) -> None:
    # enumerate each subproblem (of sizes 1, 2, 3, ...)
    # for each subproblem, check if connected
    # create the following query
    #  SELECT COUNT(*)
    #  FROM relations
    #  WHERE  filter_predicates AND join_predicates;
    n = len(join_graph.relations)
    output_dir = config['output_dir'] + query_name
    Path(output_dir).mkdir(exist_ok=True)

    query_file_dir = f'{config["output_dir"]}/{query_name}/{query_name}_cardinalities/'
    Path(query_file_dir).mkdir(exist_ok=True)

    cardinality_file = f'{query_name}_injected_cardinalities.json'
    cardinality_text = '{\n'
    cardinality_text += f'\t"result_db": [\n'
    for i in range(n + 1):
        for subproblem in itertools.combinations(join_graph.relations,  i):
            S: set[Relation] = set(subproblem)
            # check connectedness
            if not join_graph.connected(S):
                continue

            total_num_filters = 0
            select_clause = 'SELECT COUNT(*)'
            from_clause = 'FROM'
            for idx, r in enumerate(S):
                total_num_filters += len(r.filters)
                if idx != 0:
                    from_clause += ','
                from_clause += f'\n\t{r.name} AS {r.alias}'

            joins = join_graph.get_joins(S)
            if (total_num_filters == 0 and len(joins) == 0):
                # edge case: we do not produce an empty where clause if no filters and no joins are present
                where_clause = ''
            else:
                where_clause = 'WHERE'
                num_filter = 0
                for r in S:
                    for f in r.filters: # add filters
                        if num_filter != 0:
                            where_clause += ' AND'
                        where_clause += f'\n\t{f}'
                        num_filter += 1

                # compute join predicates
                if total_num_filters != 0 and len(joins) !=0:
                    where_clause += ' AND'
                for idx, join in enumerate(join_graph.get_joins(S)):
                    for lhs_attr, rhs_attr in zip(join.left_attributes, join.right_attributes):
                        join_predicate = f'{join.left_relation.alias}.{lhs_attr} = {join.right_relation.alias}.{rhs_attr}'
                        where_clause += f'\n\t{join_predicate}'
                        if idx != len(joins) - 1:
                            where_clause += ' AND'

            query = f'{select_clause}\n{from_clause}\n{where_clause};'

            query_file = f'{query_name}'
            for r in S:
                query_file += f'-{r}'
            query_file += '.sql'
            write_to_file(query_file_dir, query_file, query, 'w')

            # use postgres to execute each file and compute count(*)
            command = f"psql -U {config['user']} -d {query_name} -f {query_file_dir}/{query_file} | sed '3!d'"

            completed_proc = subprocess.run(command, capture_output=True, text=True, shell=True)
            return_code = completed_proc.returncode
            # TODO: the exit code of a pipeline is the exit code of the last command, i.e. not the psql command
            if return_code: # something went wrong during execution
                print(f'Failure during execution of `{command}` with return code {return_code}.')
            cardinality = completed_proc.stdout.strip() # remove whitespaces

            # write cardinality file
            relation_aliases = [ r.alias for r in S]
            line = f'"relations": {json.dumps(relation_aliases)}, "size": {cardinality}'
            cardinality_text += '\t\t{' + line + '}'
            if (len(S) != join_graph.num_relations()):
                cardinality_text += ','
            cardinality_text += '\n'

    cardinality_text += '\t]\n'
    cardinality_text += '}'
    write_to_file(output_dir, cardinality_file, cardinality_text, 'w')

def generate_mutable_benchmark_file(workload: str, query_name: str, query: str, directory: str, data: str):
    return f"""description: {query_name} post-join.
suite: result-db
benchmark: {workload}
name: {query_name}
readonly: true
chart:
    x:
        scale: linear
        type: O
        label: JOB Queries
    y:
        scale: linear
        type: Q
        label: 'Execution time [ms]'
    # Defaults: scale is "linear", type is "Q", label is "X" or "Y"
data:{data}

systems:
    mutable:
        args: >-
          --backend WasmV8
          --no-simd
          --cardinality-estimator Injected
          --use-cardinality-file {directory}/{query_name}_injected_cardinalities.json
          --insist-no-rehashing
          --hash-table-implementation Chained
        configurations:
            'WasmV8, single-table':
                args: ''
                pattern: '^Execute machine code:.*'
        cases:
            0: {query}
"""


def generate_post_join_files(query: str, config):
    """ Generate the files required for the post-join:
        1. <query>_resultdb.sql: contains the queries that compute the reduced relations & copies them into specific files
        2. create join graph for query based on the reduced relations
        3. create and execute setup_postgres.sh: setup file for postgres
            a. <query>_postgres_schema.sql: contains the schema for the reduced relations
            b. <query>_postgres_indexes.sql: contains the corresponding indexes on the reduced relations
        4. <query>.sql: contains the query to execute (same for mutable and postgres)
        5. <query>_injected_cardinalities.json: contains the true cardinalities of the remaining query
        6. <query>_benchmark.yml: contains the benchmark code for mutable
    """
    ########## 1. Generate the reduced relations ##########
    Path(config['output_dir']).mkdir(exist_ok=True)
    output_dir = config['output_dir'] + query
    Path(output_dir).mkdir(exist_ok=True)
    result_db_filename = f'{query}_resultdb.sql'
    workload_name = "job" if config['database'] == "imdb" else "star"

    query_graph: JoinGraph = getattr(q_def, f"create_{query}")() # execute the function `create_<query>` of module `q_def`

    projections = defaultdict(set)
    original_projections = defaultdict(set)
    filters = []

    # relations
    from_clause = f'FROM'
    for i, r in enumerate(query_graph.relations):
        for p in r.projections:
            projections[r].add(p)
            original_projections[r].add(p)
        for f in r.filters:
            filters.append(f)
        if i != 0:
            from_clause += ','
        from_clause += f' {r} AS {r.alias}'

    # filter
    where_clause = f' WHERE'
    for i, f in enumerate(filters):
        if i != 0:
            where_clause += ' AND'
        where_clause += f' {f}'

    # joins
    if filters:
        where_clause += ' AND'
    for idx, join in enumerate(query_graph.joins):
        for lhs_attr, rhs_attr in zip(join.left_attributes, join.right_attributes):
            join_predicate = f'{join.left_relation.alias}.{lhs_attr} = {join.right_relation.alias}.{rhs_attr}'
            where_clause += f' {join_predicate}'
            if idx != len(query_graph.joins) - 1: # do NOT emit `AND` for last join predicate
                where_clause += ' AND'

    query_body = f'{from_clause}{where_clause}'

    joins_between_relations_in_select = []
    # compute the extended set of relations and attributes required for post-join
    for start, end in itertools.combinations(projections.keys(), 2):
        # TODO: we might have to compute the minimal connected subgraph for projections that are not directly connected, for
        # now just compute the shortest path for all combinations of relations
        relations_on_shortest_path = shortest_path(query_graph, start, end)
        # iterate over shortest_path
        for i in range(len(relations_on_shortest_path) - 1):
            # take join  of shortest_path[i] and shortest_path[i+1] and add join attributes to projections
            join = query_graph.get_join(relations_on_shortest_path[i], relations_on_shortest_path[i+1])
            if not join in joins_between_relations_in_select:
                joins_between_relations_in_select.append(join)
                projections[join.left_relation].update(join.left_attributes)
                projections[join.right_relation].update(join.right_attributes)

    # query_body is the same for all queries: create for each relation the corresponding SELECT clause
    query_count = 0
    for r, projs in sorted(projections.items(), key=lambda e: e[0].name):
        select_clause = 'SELECT DISTINCT'
        for i, attr in enumerate(projs):
            if i != 0:
                select_clause += ','
            select_clause += f' {r.alias}.{attr}'
        reduced_relation_filename = f'{query}_{r.name}.csv'
        copy_query = f"\copy ({select_clause} {query_body}) TO '{output_dir}/{reduced_relation_filename}' CSV;"
        if (query_count):
            write_to_file(output_dir, result_db_filename, f'\n\n{copy_query}', 'a')
        else:
            write_to_file(output_dir, result_db_filename, copy_query, 'w')
        query_count += 1

    # generate resultdb, i.e. the filtered relations
    command = f"psql -U {config['user']} -d {config['database']} -f {output_dir}/{result_db_filename}"
    completed_proc = subprocess.run(command, capture_output=True, text=True, shell=True)
    return_code = completed_proc.returncode
    if return_code: # something went wrong during execution
        print(f'Failure during execution of `{command}` with return code {return_code} and error message: {completed_proc.stderr}.')

    ########## 2. Create join graph for 'new' query based on the reduced relations ##########
    for r, projs in projections.items():
        # modify the relations, i.e. convert to reduced relation
        r.filters = []
        r.projections = list(projs)

    join_graph = JoinGraph(projections.keys(), joins_between_relations_in_select)

    ########## 3. Create PostgreSQL setup ##########
    ## Schema
    postgres_schema_filename = 'schema_postgres.sql'
    if not "star" in query:
        postgres_schema = postgres_info.job_schema()
    else:
        postgres_schema = postgres_info.star_schema()

    query_count = 0
    for r, projs in sorted(projections.items(), key=lambda e: e[0].name): # make sure that star schema is sorted lexicographically
        r_schema = postgres_schema[r.name]
        postgres_schema_reduced = f"CREATE TABLE {r.name} ("
        for i, attr in enumerate(projs):
            if i != 0:
                postgres_schema_reduced += ','
            postgres_schema_reduced += f'\n\t{attr} {r_schema[attr]}'
        postgres_schema_reduced += f"\n);"
        if (query_count):
            write_to_file(output_dir, postgres_schema_filename, f'\n\n{postgres_schema_reduced}', 'a')
        else:
            write_to_file(output_dir, postgres_schema_filename, postgres_schema_reduced, 'w')
        query_count += 1

    ## FK Indexes
    postgres_indexes = postgres_info.indexes()
    postgres_fkindexes_filename = 'fkindexes_postgres.sql'
    relation_count = 0
    write_to_file(output_dir, postgres_fkindexes_filename, "", 'w')
    for r, projs in projections.items():
        if not r.name in postgres_indexes:
            continue # skip this relation if there  are no indexes
        r_indexes = postgres_indexes[r.name]
        r_indexes_text = ''
        if not r_indexes:
            continue # skip this relation if there are no indexes
        for attr in projs:
            try:
                create_index_statement = r_indexes[attr]
                r_indexes_text += f'{create_index_statement}\n'
            except:
                continue
        if relation_count != 0:
            write_to_file(output_dir, postgres_fkindexes_filename, r_indexes_text, 'a')
        else:
            write_to_file(output_dir, postgres_fkindexes_filename, r_indexes_text, 'w')
        relation_count += 1

    ## Setup
    postgres_setup_filename = 'setup_postgres.sh'
    postgres_setup = '#!/usr/bin/env bash\n\n'
    postgres_setup += f"USER={config['user']}\n"
    postgres_setup += f'DB_NAME="{query}"\n\n'

    # Drop and create database
    postgres_setup += 'psql -U ${USER} -d postgres -c "DROP DATABASE IF EXISTS "${DB_NAME}\n'
    postgres_setup += 'psql -U ${USER} -d postgres -c "CREATE DATABASE "${DB_NAME}\n'

    # Create tables
    postgres_setup += 'psql -U ${USER} -d ${DB_NAME} -f '
    postgres_setup += f'"$(pwd)/benchmark/result-db/post-join/{workload_name}/{query}/schema_postgres.sql"\n'

    # Import data
    for r in sorted(projections.keys(), key=lambda e: e.name):
        postgres_setup += 'psql -U ${USER} -d ${DB_NAME} -c "\copy '
        postgres_setup += f"{r.name} FROM '$(pwd)/benchmark/result-db/post-join/{workload_name}/{query}/{query}_{r.name}.csv' "
        postgres_setup += "WITH (FORMAT csv, DELIMITER ',', QUOTE '\\\"', ESCAPE '\\\\')\"\n"

    if not "star" in query: # create indexes only for JOB workload
        # Create indexes
        postgres_setup += 'psql -U ${USER} -d ${DB_NAME} -f "'
        postgres_setup += f"$(pwd)/benchmark/result-db/post-join/{workload_name}/{query}/fkindexes_postgres.sql\"\n"

    write_to_file(output_dir, postgres_setup_filename, postgres_setup)

    # Make setup file executable
    os.chmod(f'{output_dir}/{postgres_setup_filename}', os.stat(f'{output_dir}/{postgres_setup_filename}').st_mode | stat.S_IEXEC)

    # Execute setup file
    completed_proc = subprocess.run(f'{output_dir}/{postgres_setup_filename}', capture_output=True, text=True, shell=True)
    return_code = completed_proc.returncode
    if return_code: # something went wrong during execution
        print(f'Failure during execution of `{command}` with return code {return_code} and error message: {completed_proc.stderr}.')

    ########## 4. Create file containing the query ##########
    query_filename = f'{query}_query.sql'

    # use original_projections to remove those attributes from the projections that were only required for the post-join
    for r, projs in original_projections.items():
        join_graph.get_relation(r.id).projections = projs

    select_clause, from_clause, where_clause = generate_query(join_graph)
    query_text = f'{select_clause}{from_clause}{where_clause}'
    postgres_query_text = f'\\timing on\nSELECT COUNT(*){from_clause}{where_clause}\n\\timing off' # add timing commands for PostgreSQL
    write_to_file(output_dir, query_filename, postgres_query_text)

    ########## 5. Generate the cardinalities for the reduced relations ##########
    # this only works AFTER we set up the reduced postgres database
    create_injected_cardinalities(query, join_graph, config)


    # 6. Generate the benchmark file for mutable
    mutable_benchmark_filename = f'{query}_benchmark.yml'
    if not "star" in query:
        # create data & schema for mutable
        data = '\n'
        for r, projs in projections.items():
            data += f"\t'{r.name}':\n"
            data += f"\t\tfile: '{output_dir}/{query}_{r.name}.csv'\n"
            data += f"\t\tdelimiter: ','\n"
            data += f"\t\theader: 0\n"
            data += f"\t\tattributes:\n"
            for attr in projs:
                data += f"\t\t\t'{attr}': '{mutable_job_datatypes[r.name][attr]}'\n"
        data = data.replace('\t', '    ')
        benchmark_code = generate_mutable_benchmark_file("job", query, query_text, output_dir, data)
        write_to_file(output_dir, mutable_benchmark_filename, benchmark_code)
    else:
        # create data & schema for mutable
        data = '\n'
        for r, projs in sorted(projections.items(), key=lambda e: e[0].name):
            data += f"\t'{r.name}':\n"
            data += f"\t\tfile: '{output_dir}/{query}_{r.name}.csv'\n"
            data += f"\t\tdelimiter: ','\n"
            data += f"\t\theader: 0\n"
            data += f"\t\tattributes:\n"
            for attr in projs:
                data += f"\t\t\t'{attr}': '{mutable_star_datatypes[r.name][attr]}'\n"
        data = data.replace('\t', '    ')
        benchmark_code = generate_mutable_benchmark_file("star", query, query_text, output_dir, data)
        write_to_file(output_dir, mutable_benchmark_filename, benchmark_code)

if __name__ == '__main__':
    # Command Line Arguments
    parser = argparse.ArgumentParser(prog = 'Generate post-join files',
                                     description = '''Script to generate the files required for the execution of the
                                     post-join in mutable and PostgreSQL.''')

    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-d", "--database", default='imdb')
    parser.add_argument("-q", "--queries", default=["imdb"], nargs='+', type=str)
    parser.add_argument("-o", "--output_dir", default="benchmark/result-db/post-join/job/")

    args = parser.parse_args()
    config: dict[str, Any] = vars(args)

    if "imdb" in config['queries']: # execute all imdb queries
        assert len(config['queries']) == 1, "list of queries may only contain 'imdb' or actual queries"
        config['queries'] = [
                             "q1a",
                             "q2a",
                             "q3b",
                             "q4a",
                             "q5b",
                             "q6a",
                             "q7b",
                             "q8d",
                             "q9b",
                             "q10a",
                             "q13a",
                             "q17a",
                            ]
    elif "star" in config['queries']: # execute all star queries
        assert len(config['queries']) == 1, "list of queries may only contain 'star' or actual queries"
        config['queries'] = [
                             'star_sel_10',
                             'star_sel_20',
                             'star_sel_30',
                             'star_sel_40',
                             'star_sel_50',
                             'star_sel_60',
                             'star_sel_70',
                             'star_sel_80',
                             'star_sel_90',
                             'star_sel_100',
                            ]

    if __debug__: print('Configuration:', config)

    for query in config['queries']:
        generate_post_join_files(query, config)
