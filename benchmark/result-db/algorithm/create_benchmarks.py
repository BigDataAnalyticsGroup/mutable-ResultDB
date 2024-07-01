import argparse
import os
import re
import sys

# Get the absolute path of the utils/ directory
utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils'))
# Add utils_path to the Python path
sys.path.append(utils_path)

from query_utility import JoinGraph
import query_definitions as q_def

def parse_schema(file: str) -> dict[str, dict[str, str]]:
    with open(file, "r") as schema_file:
        mutable_schema: dict[str, dict[str, str]] = dict()  # maps relation to dict (mapping column_name to datatype)
        schema = schema_file.read()
        matches = re.finditer(r"CREATE TABLE (\w+) \((.*?)\);", schema, re.DOTALL)
        for match in matches:
            table_name = match.group(1)
            attributes = match.group(2)
            attr_dict: dict[str, str] = dict()  # maps column_name to datatype
            for attr in attributes.split(","):
                attr = attr.strip()
                if not attr:
                    continue
                attr_name, attr_type = attr.split(maxsplit=1)
                attr_type = re.sub(r"INT\(\d+\)", "INT", attr_type)
                attr_type = re.sub(r"CHAR\((\d+)\)", r"CHAR \1", attr_type)
                attr_dict[attr_name] = attr_type
            mutable_schema[table_name] = attr_dict
        return mutable_schema

def create_benchmark_file(query: str, schema: dict[str, dict[str, str]]) -> None:
    join_graph: JoinGraph = getattr(q_def, f"create_q{query}")() # execute the function `create_<query>` of module `q_def`
    relation_names = [r.name for r in join_graph.relations]
    data = '\n'
    for r in relation_names:
        data += f"\t'{r}':\n"
        data += f"\t\tfile: 'benchmark/job/data/{r}.csv'\n"
        data += f"\t\tformat: 'csv'\n"
        data += f"\t\tdelimiter: ','\n"
        data += f"\t\theader: 0\n"
        data += f"\t\tattributes:\n"
        for attr, datatype in schema[r].items():
            data += f"\t\t\t'{attr}': '{datatype}'\n"
        data = data.replace('\t', '    ')

    with open(f"./benchmark/job/mutable/{query}.sql", 'r') as mutable_file:
        mutable_query = mutable_file.read().split("\n\n")[1] # split at "\n\n" to remove import statements
        mutable_query = " ".join(mutable_query.splitlines()).strip() # convert to single line to ensure correct formatting
        mutable_query = mutable_query.replace('\t', "")
    benchmark = f"""description: Join-Order Benchmark q{query}.
suite: result-db
benchmark: job
name: q{query}
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
          --use-cardinality-file benchmark/result-db/algorithm/job/q{query}_cardinalities.json
          --insist-no-rehashing
        configurations:                                   # Different experiment configurations.
            'WasmV8, resultdb':
                args: --result-db
                pattern: '^Execute machine code:.*'
            'WasmV8, decompose':
                args: --decompose
                pattern: '^Execute machine code:.*'
            'WasmV8, single-table':
                args: ''
                pattern: '^Execute machine code:.*'
        cases:
            0: \'{mutable_query}\'
"""
    with open(f"./benchmark/result-db/algorithm/job/q{query}_benchmark.yml", 'w') as benchmark_file:
        benchmark_file.write(benchmark)

if __name__ == "__main__":
    # Command Line Arguments
    parser = argparse.ArgumentParser(
        prog="Create mutable benchmark files for JOB queries",
        description="""Script to create mutable benchmark files.""",
    )

    parser.add_argument("-q", "--queries", default=["imdb"], nargs="+", type=str)

    args = parser.parse_args()
    config = vars(args)

    job_queries = [
        "1a",  "1b",  "1c",  "1d",
        "2a",  "2b",  "2c",  "2d",
        "3a",  "3b",  "3c",
        "4a",  "4b",  "4c",
        "5a",  "5b",  "5c",
        "6a",  "6b",  "6c",  "6d",  "6e",  "6f",
        "7a",  "7b",  "7c",
        "8a",  "8b",  "8c",  "8d",
        "9a",  "9b",  "9c",  "9d",
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

    if "imdb" in config["queries"]:  # use all JOB queries
        assert len(config["queries"]) == 1, "list of queries may only contain 'imdb' or actual queries"
        config["queries"] = job_queries
    else:
        assert set(config["queries"]).issubset(job_queries), print(config["queries"])

    mutable_schema = parse_schema( "./benchmark/result-db/algorithm/job/schema_mutable_reduced.sql" )

    for query in config["queries"]:
        create_benchmark_file(query, mutable_schema)
