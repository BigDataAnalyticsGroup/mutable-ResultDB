import argparse
import json
import re
import subprocess

from typing_extensions import TextIO


def run_postgres(file: str, user: str, database: str, out_file: TextIO, rewrite_method: bool = False) -> int | list[int]:
    command = f"psql -U {user} -d {database} -f {file}"
    completed_proc = subprocess.run(command, capture_output=True, text=True, shell=True)
    return_code = completed_proc.returncode
    if return_code:  # something went wrong during execution
        out_file.write(f'\tRunning PostgreSQL query: Failure during execution of `{command}` with return code {return_code}.')
        out_file.write(f'\t\t{completed_proc.stderr}')
        return -1 if not rewrite_method else [-1]
    output = completed_proc.stdout
    counts = re.findall(r'^\s+(\d+)\s*$', output, re.MULTILINE) # use regex to find all numbers in the `count` column
    counts = [int(count) for count in counts]
    if not rewrite_method: # single-table execution
        assert len(counts) == 1, f"Running PostgreSQL: single-table execution expects one result set size, got {len(counts)}. File: {file}"
        return counts[0]
    return counts

def run_mutable(query: str, queryfile: str, out_file: TextIO, flags: str = "") -> int | list[int]:
    command = (f"./build/release/bin/shell"
               f" --backend WasmV8"
               f" --insist-no-rehashing"
               f" --no-simd"
               f" --benchmark"
               f" {flags}"
               f" --cardinality-estimator Injected"
               f" --use-cardinality-file benchmark/result-db/algorithm/job/q{query}_cardinalities.json"
               f" benchmark/result-db/algorithm/job/schema_mutable_reduced.sql"
               f" {queryfile}")
    completed_proc = subprocess.run(command, capture_output=True, text=True, shell=True)
    return_code = completed_proc.returncode
    if return_code:  # something went wrong during execution
        out_file.write(f"\tRunning mutable query: Failure during execution of `{command}` with return code {return_code}.")
        out_file.write(f"\t\t{completed_proc.stderr}")
        return -1 if not flags else [-1]
    output = completed_proc.stdout
    rows_lines = re.findall(r'^\d+\s+rows$', output, re.MULTILINE) # use regex to match lines with "<number> rows"
    counts = [ int(e.split()[0]) for e in rows_lines ]
    if not flags: # single-table execution
        assert len(counts) == 1, f"Running mutable {query}: single-table execution expects one result set size, got {len(counts)}"
        return counts[0]
    return counts

def extract_cardinality(file: str) -> int:
    with open(file, mode='r') as cardinality_file:
        final_cardinality_line = cardinality_file.readlines()[-3]
        parsed_line = json.loads(final_cardinality_line.strip()) # parse line in json format
        cardinality = int(parsed_line.get("size"))
        return cardinality


if __name__ == '__main__':
    # Command Line Arguments
    parser = argparse.ArgumentParser(prog = 'Generate JOB query graphs',
                                     description = '''Script to generate JOB query graphs.''')

    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-d", "--database", default='imdb')
    parser.add_argument("-q", "--queries", default=["imdb"], nargs='+', type=str)

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
        "9b",  "9a",  "9c",  "9d",
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

    postgres_queries_original = "./benchmark/job/postgres/" # rewritten to SELECT COUNT(*)
    mutable_queries = "./benchmark/job/mutable/" # generated using query definitions
    postgres_rewrites = "./benchmark/result-db/rewrite-methods/job/"
    mutable_cardinalities = "./benchmark/result-db/algorithm/job/"
    with open('verify.txt', 'w', buffering=1) as out_file:
        for query in config['queries']:
            out_file.write(f"Running query: {query}\n")
            # Single Table
            out_file.write(f"\tSingle Table results:\n")
            postgres_st_og_count = run_postgres(f'{postgres_queries_original}{query}.sql', config['user'], config['database'], out_file)  # original query
            out_file.write(f"\t\tPostgreSQL original: {postgres_st_og_count}\n")
            postgres_st_gen_count = run_postgres(f'{postgres_rewrites}q{query}/q{query}_default.sql', config['user'], config['database'], out_file)  # query generated based on query definition
            out_file.write(f"\t\tPostgreSQL generated: {postgres_st_gen_count}\n")
            mutable_st_count = run_mutable(query, f'{mutable_queries}{query}.sql', out_file)
            out_file.write(f"\t\tmutable generated: {mutable_st_count}\n")
            cardinality = extract_cardinality(f"{mutable_cardinalities}q{query}_cardinalities.json")
            out_file.write(f"\t\tCardinality: {cardinality}\n")
            if not (postgres_st_og_count == postgres_st_gen_count == mutable_st_count == cardinality):
                out_file.write(f"\t\t-> ERROR: results do not match\n\n")

            # ResultDB
            out_file.write(f"\tResult DB results:\n")
            postgres_rm1_counts = run_postgres(f"{postgres_rewrites}q{query}/q{query}_RM1.sql", config['user'], config['database'], out_file, rewrite_method=True)
            out_file.write(f"\t\tPostgreSQL RM1: {postgres_rm1_counts}\n")
            postgres_rm2_counts = run_postgres(f"{postgres_rewrites}q{query}/q{query}_RM2.sql", config['user'], config['database'], out_file, rewrite_method=True)
            out_file.write(f"\t\tPostgreSQL RM2: {postgres_rm2_counts}\n")
            postgres_rm3_counts = run_postgres(f"{postgres_rewrites}q{query}/q{query}_RM3.sql", config['user'], config['database'], out_file, rewrite_method=True)
            out_file.write(f"\t\tPostgreSQL RM3: {postgres_rm3_counts}\n")
            postgres_rm4_counts = run_postgres(f"{postgres_rewrites}q{query}/q{query}_RM4.sql", config['user'], config['database'], out_file, rewrite_method=True)
            out_file.write(f"\t\tPostgreSQL RM4: {postgres_rm4_counts}\n")
            mutable_rdb_counts = run_mutable(query, f"{mutable_queries}{query}.sql", out_file, flags="--result-db")
            out_file.write(f"\t\tmutable Result DB: {mutable_rdb_counts}\n")
            mutable_decomp_counts = run_mutable(query, f"{mutable_queries}{query}.sql", out_file, flags="--decompose")
            out_file.write(f"\t\tmutable Decompose: {mutable_decomp_counts}\n")
            if not (sorted(postgres_rm1_counts) == sorted(postgres_rm2_counts) == sorted(postgres_rm3_counts) == sorted(postgres_rm4_counts) == sorted(mutable_rdb_counts) == sorted(mutable_decomp_counts)):
                out_file.write(f"\t\t-> ERROR: results do not match\n")
