import argparse
import csv
import glob
import os
import subprocess
from typing import Any


def run_benchmarks(config) -> None:
    measurements: dict[str, list[Any]] = {
        'database': list(),
        'system': list(),
        'query': list(),
        'method': list(),
        'run': list(),
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
        files = sorted(glob.glob(f'{directory}/{q}/{q}_query.sql'))
        for f in files: # iterate over all files in rewrite-methods/<query>/*.sql
            for n in range(config['num_runs']):

                command = f"psql -U {config['user']} -d {q} -f {f} | grep 'Time: [0-9]*.[0-9]* ms' | cut -d ' ' -f 2"
                # execute command -> returns `CompletedProcess` object
                completed_proc = subprocess.run(command, capture_output=True, text=True, shell=True)
                return_code = completed_proc.returncode
                # TODO: the exit code of a pipeline is the exit code of the last command, i.e. not the psql command
                if return_code: # something went wrong during execution
                    print(f'Failure during execution of `{command}` with return code {return_code}.')
                time = float(completed_proc.stdout)
                if not time:
                    print(f'file: {f} >>> No output!')

                measurements['database'].append(database)
                measurements['system'].append("postgres")
                measurements['query'].append(q)
                measurements['method'].append("post_join")
                measurements['run'].append(n)
                measurements['time'].append(time)
                print(f'\tFinished run {n} of file {f}')

        # write measurements to csv file
        with open(f'{directory}/postjoin-postgres-results.csv', 'w', newline='\n') as csv_file:
            field_names = measurements.keys()
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()

            num_measurements = len(measurements['database'])
            for i in range(num_measurements):
                writer.writerow({'database': measurements['database'][i],
                                 'system': measurements['system'][i],
                                 'query': measurements['query'][i],
                                 'method': measurements['method'][i],
                                 'run': measurements['run'][i],
                                 'time': measurements['time'][i]})

        print(f'Finished {q}.')


########################################################################################################################
# Main
########################################################################################################################
if __name__ == '__main__':
    # Command Line Arguments
    parser = argparse.ArgumentParser(prog = 'Run post-join experiments.',
                                     description = '''Run the post-join experiments in PostgreSQL.''')

    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-d", "--database", default='imdb')
    parser.add_argument("-n", "--num_runs", default=5, type=int)
    parser.add_argument("-q", "--queries", default=[], nargs='+', type=str)
    parser.add_argument("--directory", default="benchmark/result-db/post-join/job/", type=str)

    args = parser.parse_args()
    config: dict[str, Any] = vars(args)

    job_queries = [
        "q3c",
        "q4a",
        "q9c",
        "q11c",
        "q16a",
        "q18c",
        "q22c",
        "q25b",
        "q28c",
        "q33c",
    ]

    if "imdb" in config["queries"]:  # use all JOB queries
        assert len(config["queries"]) == 1, "list of queries may only contain 'imdb' or actual queries"
        config["queries"] = job_queries
    else:
        assert set(config["queries"]).issubset(job_queries), print(config["queries"])

    if __debug__: print('Configuration:', config)

    # Setup
    run_benchmarks(config)
