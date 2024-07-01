import argparse
import csv
import glob
import os
import subprocess
from typing import Any

METHODS: dict[str, str] = {
    "default": "0. Single Table",
    "RM1": "RM1. Dynamic SELECT DISTINCT",
    "RM2": "RM2. Materialized SELECT DISTINCT",
    "RM3": "RM3. Dynamic Subquery",
    "RM4": "RM4. Materialized Subquery"
}

def run_benchmarks(config) -> None:
    measurements: dict[str, list[Any]] = {
        'database': list(),
        'system': list(),
        'query': list(),
        'method': list(),
        'data_transfer': list(),
        'run': list(),
        'num_query_internal': list(),
        'time': list()
    }

    queries: list[str] = config['queries']
    database: str = config['database']
    directory: str = config['directory']

    if (not queries):
        print(f'No queries provided. Benchmark script will not run.')

    for q in queries:
        # execute the queries
        if not os.path.isdir(f'{directory}/{q}'):
            print(f'No {q} directory found. Skipping.')
            continue
        files = sorted(glob.glob(f'{directory}/{q}/*.sql'))
        for f in files: # iterate over all files in rewrite-methods/<query>/*.sql
            for n in range(config['num_runs']):
                basename = os.path.basename(f).rsplit('.')[0]
                query_name = basename.rsplit('_', 1)[0]
                if "data-transfer" in query_name: # remove superfluous "data-transfer" from query name
                    query_name = query_name.rsplit('_', 1)[0]
                if config['workload'] == "post-join":
                    query_name = query_name.split('_')[0]
                method = basename.rsplit('_', 1)[1]
                data_transfer = "data-transfer" in f

                command = f"psql -U {config['user']} -d {database} -f {f} | grep 'Time: [0-9]*.[0-9]* ms' | cut -d ' ' -f 2"
                # execute command -> returns `CompletedProcess` object
                completed_proc = subprocess.run(command, capture_output=True, text=True, shell=True)
                return_code = completed_proc.returncode
                # TODO: the exit code of a pipeline is the exit code of the last command, i.e., not the psql command
                if return_code: # something went wrong during execution
                    print(f'Failure during execution of `{command}` with return code {return_code}.')
                output = completed_proc.stdout.strip().split('\n') # split output string into individual timings
                if not output:
                    print(f'file: {f} >>> No output!')
                # num_query_internal: the query number inside the file (e.g. the materialized view has multiple queries
                # for computing the mat. view and subsequently computing the individual result sets -> this allows
                # for more flexibility when creating the graphs
                for num_query_internal, time in enumerate(output):
                    measurements['database'].append(database)
                    measurements['system'].append("postgres")
                    measurements['query'].append(query_name)
                    measurements['method'].append(METHODS[method])
                    measurements['data_transfer'].append(data_transfer)
                    measurements['run'].append(n)
                    measurements['num_query_internal'].append(num_query_internal)
                    measurements['time'].append(time)
                print(f'\tFinished run {n} of file {f}')

        # write measurements to csv file
        outputfile = "rewrite-results.csv" if config['workload'] == "job" else "rewrite-results-post-join.csv"
        with open(f'{directory}/{outputfile}', 'w', newline='\n') as csv_file:
            field_names = measurements.keys()
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()

            num_measurements = len(measurements['database'])
            for i in range(num_measurements):
                writer.writerow({'database': measurements['database'][i],
                                 'system': measurements['system'][i],
                                 'query': measurements['query'][i],
                                 'method': measurements['method'][i],
                                 'data_transfer': measurements['data_transfer'][i],
                                 'run': measurements['run'][i],
                                 'num_query_internal': measurements['num_query_internal'][i],
                                 'time': measurements['time'][i]})

        print(f'Finished {q}.')


########################################################################################################################
# Main
########################################################################################################################
if __name__ == '__main__':
    # Command Line Arguments
    parser = argparse.ArgumentParser(prog = 'Rewrite Benchmark',
                                     description = '''Benchmark Framework for the execution of rewritten queries in the
                                     context of SELECT RESULTDB.''')

    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-d", "--database", default='imdb')
    parser.add_argument("-n", "--num_runs", default=5, type=int)
    parser.add_argument("-q", "--queries", default=[], nargs='+', type=str)
    parser.add_argument("-w", "--workload", default="job")
    parser.add_argument("--directory", default="benchmark/result-db/rewrite-methods/job/", type=str)

    args = parser.parse_args()
    config: dict[str, Any] = vars(args)

    job_queries = [
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
    post_join_queries = [
            "q3c_pj",
            "q4a_pj",
            "q9c_pj",
            "q11c_pj",
            "q16b_pj",
            "q18c_pj",
            "q22c_pj",
            "q25b_pj",
            "q28c_pj",
            "q33c_pj",
    ]

    if config['workload'] == "job":
        if "imdb" in config['queries']: # execute all imdb queries
            assert len(config['queries']) == 1, "list of queries may only contain 'imdb' or actual queries"
            config['queries'] = job_queries
        else:
            assert set(config["queries"]).issubset(job_queries), print(config["queries"])
    elif config['workload'] == "post-join":
        config['queries'] = post_join_queries
    else:
        print("'--workload' has to be either 'job' or 'post-join'")
        exit(1)

    if __debug__: print('Configuration:', config)

    # Setup
    run_benchmarks(config)
