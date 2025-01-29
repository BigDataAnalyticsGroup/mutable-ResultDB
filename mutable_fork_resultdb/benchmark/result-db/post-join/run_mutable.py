import subprocess
import argparse

job_queries = [
    "q3c",
    "q4a",
    "q9c",
    "q11c",
    "q18c",
    "q22c",
    "q25b",
    "q28c",
    "q33c",
]

if __name__ == '__main__':
    # Command Line Arguments
    parser = argparse.ArgumentParser(prog = 'Run post-join experiments',
                                     description = '''Script to execute the mutable benchmarks for the post-join
                                     experiments.''')
    parser.add_argument("-w", "--workload") # currently only 'job'

    args = parser.parse_args()
    config = vars(args)

    workload = config['workload']
    queries = job_queries

    for q in queries:
        subprocess.run(f'python benchmark/Benchmark.py --verbose ./benchmark/result-db/post-join/{workload}/{q}/{q}_benchmark.yml --output ./benchmark/result-db/post-join/{workload}/{q}/{q}_results.csv', shell=True)
