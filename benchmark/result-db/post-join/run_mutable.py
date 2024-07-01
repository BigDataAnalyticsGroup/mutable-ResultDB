import subprocess
import argparse

job_queries = [
    "q1b",
    "q2a",
    "q3c",
    "q4a",
    "q5c",
    # "q6a",  "q6b",  "q6c",  "q6d",  "q6e",  "q6f",
    "q7a",
    "q8a",
    "q9c",
    "q10c",
    "q11c",
    "q12a",
    # "q13a", "q13b", "q13c", "q13d",
    "q14a",
    "q15d",
    # "q16a", "q16b", "q16c", "q16d",
    # "q17a", "q17b", "q17c", "q17d", "q17e", "q17f",
    "q18c",
    "q19a",
    # "q20a", "q20b", "q20c",
    "q21a",
    "q22c",
    "q23a",
    "q24a",
    "q25b",
    "q26a",
    "q27a",
    "q28c",
    # "q29a", "q29b", "q29c",
    "q30c",
    "q31a",
    # "q32a", "q32b",
    "q33c",
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
