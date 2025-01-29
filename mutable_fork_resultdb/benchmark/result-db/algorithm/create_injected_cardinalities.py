import argparse
import subprocess
import json
from itertools import combinations
from pathlib import Path
from typing import Any
import sys
import os

# Get the absolute path of the utils/ directory
utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils'))
# Add utils_path to the Python path
sys.path.append(utils_path)

from query_utility import Relation, JoinGraph
import query_definitions as q_def


DATABASE='result_db'

def write_to_file(output_file: str, text: str, mode: str):
    with open(output_file, mode) as file:
        file.write(text)

def create_injected_cardinalities(query_name: str, config) -> None:
    # enumerate each subproblem (of sizes 1, 2, 3, ...)
    # for each subproblem, check if connected
    # create the following query
    #  SELECT COUNT(*)
    #  FROM relations
    #  WHERE  filter_predicates AND join_predicates;
    join_graph: JoinGraph = getattr(q_def, f"create_{query_name}")() # execute the function `create_<query_name>` of module `q_def`
    n = len(join_graph.relations)
    query_file_dir = f'{config["output_dir"]}{query_name}_cardinalities/'
    Path(query_file_dir).mkdir(exist_ok=True)

    cardinality_file = f'{config["output_dir"]}/{query_name}_cardinalities.json'
    cardinality_text = '{\n'
    cardinality_text += f'\t"{DATABASE}": [\n'
    for i in range(n + 1):
        for subproblem in combinations(join_graph.relations,  i):
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

            query_file = f'{query_file_dir}{query_name}'
            for r in S:
                query_file += f'-{r}'
            query_file += '.sql'
            write_to_file(query_file, query, 'w')

            # use postgres to execute each file and compute count(*)
            command = f"psql -U {config['user']} -d {config['database']} -f {query_file} | sed '3!d'"

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
    write_to_file(cardinality_file, cardinality_text, 'w')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = 'Generate Injected Cardinalities',
                                     description = '''Compute the real cardinality for each subproblem of a given query
                                     using PostgreSQL.''')

    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-d", "--database", default="imdb")
    parser.add_argument("-q", "--queries", default=["imdb"], nargs='+', type=str)
    parser.add_argument("-o", "--output_dir", default="benchmark/result-db/algorithm/job/")

    args = parser.parse_args()
    config: dict[str, Any] = vars(args)

    if "imdb" in config['queries']: # execute all imdb queries
        assert len(config['queries']) == 1, "list of queries may only contain 'imdb' or actual queries"
        config['queries'] = [
            "q1a",  "q1b",  "q1c",  "q1d",
            "q2a",  "q2b",  "q2c",  "q2d",
            "q3a",  "q3b",  "q3c",
            "q4a",  "q4b",  "q4c",
            "q5a",  "q5b",  "q5c",
            "q6a",  "q6b",  "q6c",  "q6d",  "q6e",  "q6f",
            "q7a",  "q7b",  "q7c",
            "q8a",  "q8b",  "q8c",  "q8d",
            "q9a",  "q9b",  "q9c",  "q9d",
            "q10a", "q10b", "q10c",
            "q11a", "q11b", "q11c", "q11d",
            "q12a", "q12b", "q12c",
            "q13a", "q13b", "q13c", "q13d",
            "q14a", "q14b", "q14c",
            "q15a", "q15b", "q15c", "q15d",
            "q16a", "q16b", "q16c", "q16d",
            "q17a", "q17b", "q17c", "q17d", "q17e", "q17f",
            "q18a", "q18b", "q18c",
            "q19a", "q19b", "q19c", "q19d",
            "q20a", "q20b", "q20c",
            "q21a", "q21b", "q21c",
            "q22a", "q22b", "q22c", "q22d",
            "q23a", "q23b", "q23c",
            "q24a", "q24b",
            "q25a", "q25b", "q25c",
            "q26a", "q26b", "q26c",
            "q27a", "q27b", "q27c",
            "q28a", "q28b", "q28c",
            "q29a", "q29b", "q29c",
            "q30a", "q30b", "q30c",
            "q31a", "q31b", "q31c",
            "q32a", "q32b",
            "q33a", "q33b", "q33c",
        ]

    if __debug__: print('Configuration:', config)

    for query in config['queries']:
        print(f"Generating cardinalities for {query}")
        create_injected_cardinalities(query, config)
