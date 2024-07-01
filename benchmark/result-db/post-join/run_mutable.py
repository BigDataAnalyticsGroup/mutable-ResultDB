import subprocess
import argparse

job_queries = [
               "q1a",
               "q3b",
               "q4a",
               "q5b",
              ]

star_queries = [
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

if __name__ == '__main__':
    # Command Line Arguments
    parser = argparse.ArgumentParser(prog = 'Run post-join experiments',
                                     description = '''Script to execute the mutable benchmarks for the post-join
                                     experiments.''')
    parser.add_argument("-w", "--workload") # either 'job' or 'star'

    args = parser.parse_args()
    config = vars(args)

    workload = config['workload']
    queries = job_queries if workload == 'job' else star_queries

    for q in queries:
        subprocess.run(f'python benchmark/Benchmark.py --verbose ./benchmark/result-db/post-join/{workload}/{q}/{q}_benchmark.yml --output ./benchmark/result-db/post-join/{workload}/{q}/{q}_results.csv', shell=True)
