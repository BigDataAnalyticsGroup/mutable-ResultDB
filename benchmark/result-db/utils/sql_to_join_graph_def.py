import argparse
import re
import os
from collections import defaultdict

from dataclasses import dataclass


@dataclass
class JGComponents:
    alias_to_relation: dict[str, str]
    projections: dict[str, list[str]]
    filters: dict[str, list[str]]
    attributes: dict[str, set[str]]
    joins: dict[tuple[str, str], tuple[str, str]]


def generate_join_graph_components(input_file:str, mutable:bool = False) -> JGComponents:
    with (open(input_file, 'r') as f):
        query_name = os.path.basename(input_file).split('.')[0]
        sql_query = f.read()
        # Regular expression to match SQL clauses
        pattern = r"(SELECT.*?)(?=FROM)|(\bFROM.*?)(?=WHERE)|(\bWHERE.*?);"
        matches = re.findall(pattern, sql_query, re.DOTALL | re.IGNORECASE)

        # Combine non-empty matches and append semicolon
        split_query: list[str] = [clause.strip() for match in matches for clause in match if clause.strip()]
        assert(len(split_query) == 3)
        select_clause: str = split_query[0]
        from_clause: str = split_query[1]
        where_clause: str = split_query[2]

        # gather all attributes for a given alias
        attributes: dict[str, set[str]] = defaultdict(set)

        # Extract projections from SELECT clause
        pattern = r"\((.*?)\)"
        matches = re.findall(pattern, select_clause) # matches everything in parentheses (..)
        matches = [ m.split('.') for m in matches ] # converts "alias.attribute" into ["alias", "attribute"]
        # Create a dictionary with alias as keys and column names as values
        projections: dict[str, list[str]] = defaultdict(list)
        for alias, attr in matches:
            projections[alias].append(attr)
            attributes[alias].add(attr)

        # Extract relation name and alias from FROM clause
        pattern = r"(\w+)\s+AS\s+(\w+)" # regular expression to match relation names and their aliases
        matches = re.findall(pattern, from_clause)
        # Create a dictionary mapping aliases to relation names
        alias_to_relation: dict[str, str] = {alias: relation for relation, alias in matches}

        # Extract filters and joins from WHERE clause
        # rewrite BETWEEN statement to two independent clauses (to get rid of "AND" keyword which is used later to split the clauses)
        where_clause = re.sub(r"(\S+)\s+BETWEEN (\d+) AND (\d+)",
                              r"\1 >= \2 AND \1 <= \3",
                              where_clause) # rewrite "r.a BETWEEN x AND y" to "r.a >= x AND r.a <= y"
        clauses: list[str] = where_clause.replace("WHERE", "").split("AND") # remove WHERE and split in clauses
        clauses: list[str] = [ c.strip() for c in clauses ] # remove leading and trailing whitespaces, newlines, etc.
        filters: dict[str, list[str]] = defaultdict(list) # maps alias to filter
        joins: dict[tuple[str, str], tuple[str, str]] = dict() # maps two aliases (relations) to two attributes (join predicate)

        def is_join_predicate(condition: str) -> bool:
            # define a regex pattern for a join predicate
            pattern = r"^\s*\w+\.\w+\s*=\s*\w+\.\w+\s*$"  # matches "table1.column1 = table2.column2"
            # check if the condition matches the pattern
            return bool(re.match(pattern, condition))

        for clause in clauses: # iterate over each clause
            if "IN" in clause:
                # rewrite "r.a IN ('x', 'y')" -> "r.a = 'x' OR r.a = 'y'"
                split_clause = clause.split('IN')
                relation_attribute = split_clause[0].strip() # r.a
                alias, attr = relation_attribute.split('.')
                conditions = split_clause[1].strip()[1:-1] # remove whitespaces and outer parentheses
                conditions = [ c.strip() for c in conditions.split(',') ] # split conditions at ',' and remove whitespaces
                or_conditions = " OR ".join([f'{relation_attribute} = {c}' for c in conditions])
                or_conditions = '(' + or_conditions + ')'
                filters[alias].append(or_conditions)
                attributes[alias].add(attr)
                continue
            if is_join_predicate(clause):
                # clause is of the form: "table1.column1 = table2.column2"
                left, right = clause.split('=')
                left_alias, left_attribute = left.strip().split('.')
                right_alias, right_attribute = right.strip().split('.')
                attributes[left_alias].add(left_attribute)
                attributes[right_alias].add(right_attribute)
                joins[(left_alias, right_alias)] = (left_attribute, right_attribute)
                continue
            if "OR" in clause:
                # clause is of the form: (r.a = x OR r.a = y)
                clause = re.sub(r'\s+', ' ', clause.replace('\n', '')).strip() # remove newlines and multiple whitespaces
                pattern = r"(\w+)\.(\w+)"  # regular expression to capture the table/alias name and column name
                matches = re.findall(pattern, clause)
                assert matches
                assert all(t == matches[0] for t in matches), "Not all relation/attribute pairs are equal in OR clause"
                alias, attr = matches[0]
                filters[alias].append(clause)
                attributes[alias].add(attr)
                continue
            if "IS" in clause and mutable: # only required for mutable -> not required for postgres
                # rewrite "r.a IS (NOT) NULL" -> "(NOT) ISNULL(r.a)"
                pattern = r"(\w+)\.(\w+)"  # regular expression to capture the table/alias name and column name
                match = re.match(pattern, clause)
                assert match, f"query: {query_name} | clause: {clause}"
                alias, attr = match.groups()
                new_clause = f"ISNULL({alias}.{attr})"
                new_clause = "NOT " + new_clause if "NOT" in clause else new_clause
                filters[alias].append(new_clause)
                attributes[alias].add(attr)
                continue
            # regular filter
            pattern = r"(\w+)\.(\w+)"  # regular expression to capture the table/alias name and column name
            match = re.match(pattern, clause)
            assert match, f"regular filter -- query: {query_name} | clause: {clause}"
            alias, attr = match.groups()
            if "NOT LIKE" in clause and mutable:
                # rewrite "r.a NOT LIKE <pattern>" -> "NOT r.a LIKE <pattern>"
                clause = re.sub("([^ \n]*) NOT LIKE", r"NOT \1 LIKE", clause)
            filters[alias].append(clause)
            attributes[alias].add(attr)

    return JGComponents(alias_to_relation, projections, filters, attributes, joins)

def parse_sql_to_mutable_query(input_file: str):
    components: JGComponents = generate_join_graph_components(input_file, mutable=True)
    imports = ""
    imported_relations = set()
    for _, relation in components.alias_to_relation.items():
        if not relation in imported_relations:
            imports += f"IMPORT INTO {relation} DSV \"benchmark/job/data/{relation}.csv\";\n"
            imported_relations.add(relation)


    query = f"\nSELECT"
    num_proj = 0
    for alias, attributes in components.projections.items():
        for proj_attr in attributes:
            if num_proj != 0:
                query += ','
            query += f"\n\t{alias}.{proj_attr}"
            num_proj += 1

    query += "\nFROM"
    for i, (alias, relation) in enumerate(components.alias_to_relation.items()):
        if i != 0:
            query += ','
        query += f"\n\t{relation} AS {alias}"

    query += "\nWHERE"
    num_filter = 0
    for alias, filters in components.filters.items():
        for filter in filters:
            if num_filter != 0:
                query += " AND"
            query += f'\n\t{filter}'
            num_filter += 1
    if components.filters:
        query += " AND"
    for i, (relations, attributes) in enumerate(components.joins.items()):
        left_relation = relations[0]
        right_relation = relations[1]
        left_attr = attributes[0]
        right_attr = attributes[1]
        query += f"\n\t{left_relation}.{left_attr} = {right_relation}.{right_attr}"
        if i != len(components.joins) - 1: # do not emit 'AND' for last join predicate
            query += " AND"

    query += ';'

    query_filename = os.path.basename(input_file)
    with open(f"./benchmark/job/mutable/{query_filename}", 'w') as out:
        query = query.replace("'", '"') # replace single quotes with double quotes for mutable
        out.write(f"{imports}{query}")

def parse_sql_to_join_graph(input_file: str):
        components: JGComponents = generate_join_graph_components(input_file)
        query_definition = f"def create_q{query_name}():\n"
        # generate relation definitions
        for alias, relation in components.alias_to_relation.items():
            proj = components.projections[alias] if alias in components.projections else "[]"
            filter = components.filters[alias] if alias in components.filters else "[]"
            assert components.attributes[alias]
            attrs = list(components.attributes[alias]) # there always has to be at least one attributes
            query_definition += f"\t{alias} = Relation(name = \"{relation}\", alias = \"{alias}\", attributes = {attrs}, filters = {filter}, projections = {proj})\n"
        query_definition += f"\trelations = [{', '.join(components.alias_to_relation.keys())}]\n\n"

        # generate joins
        join_names = []
        for i, (relations, attributes) in enumerate(components.joins.items()):
            left_alias, right_alias = relations
            left_attr, right_attr = attributes
            join_names.append(f"j{i}")
            query_definition += f"\tj{i} = Join({left_alias}, {right_alias}, [\"{left_attr}\"], [\"{right_attr}\"])\n"
        query_definition += f"\tjoins = [{', '.join(join_names)}]\n\n"
        query_definition += f"\treturn JoinGraph(relations, joins)\n\n"

        with open('./benchmark/result-db/utils/query_definitions.py', 'a') as out:
            out.write(query_definition)


if __name__ == '__main__':
    # Command Line Arguments
    parser = argparse.ArgumentParser(prog = 'Generate JOB query graphs',
                                     description = '''Script to generate JOB query graphs.''')

    parser.add_argument("-q", "--queries", default=["imdb"], nargs='+', type=str)
    parser.add_argument('--mutable', action=argparse.BooleanOptionalAction, default=False) # enable with --mutable

    args = parser.parse_args()
    config = vars(args)

    job_queries = [
        "1a", "1b", "1c", "1d",
        "2a", "2b", "2c", "2d",
        "3a", "3b", "3c",
        "4a", "4b", "4c",
        "5a", "5b", "5c",
        "6a", "6b", "6c", "6d", "6e", "6f",
        "7b",  # q7a and q7c are NOT supported
        "8a", "8b", "8c", "8d",
        "9a", "9b", "9c", "9d",
        "10a", "10b", "10c",
        "11a", "11b", "11c", "11d",
        "12a", "12b", "12c",
        "13a", "13b", "13c", "13d",
        "14a", "14b", "14c",
        "15a", "15b", "15c", "15d",
        "16a", "16b", "16c", "16d",
        "17a", "17b", "17c", "17d", "17e", "17f",
        "18a", "18b", "18c",
        "19a", "19b", "19c", "19d",
        "20a", "20b", "20c",
        "21a", "21b", "21c",
        "22a", "22b", "22c", "22d",
        "23a", "23b", "23c",
        "24a", "24b",
        "25a", "25b", "25c",
        "26a", "26b", "26c",
        "27a", "27b", "27c",
        "28a", "28b", "28c",
        "29a", "29b", "29c",
        "30a", "30b", "30c",
        "31a", "31b", "31c",
        "32a", "32b",
        "33a", "33b", "33c",
    ]

    if "imdb" in config['queries']: # execute all imdb queries
        assert len(config['queries']) == 1, "list of queries may only contain 'imdb' or actual queries"
        config['queries'] = job_queries
    else:
        assert set(config['queries']).issubset(job_queries), print(config['queries'])

    for query_name in config['queries']:
        query_file = f"./benchmark/job/join-order-benchmark/{query_name}.sql"
        if config['mutable']:
            parse_sql_to_mutable_query(query_file)
        else:
            parse_sql_to_join_graph(query_file)
