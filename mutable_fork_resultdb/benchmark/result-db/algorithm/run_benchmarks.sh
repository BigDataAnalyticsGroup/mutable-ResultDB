#!/usr/bin/env bash

if [ $# -eq 0 ]
  then
    echo "Provide which benchmarks to execute, currently only 'job' supported."
    exit 1
fi

benchmark_name="$1"

job_benchmarks=(
    "q1b"
    "q2a"
    "q3c"
    "q4a"
    "q5c"
    "q7a"
    "q8a"
    "q9c"
    "q10c"
    "q11c"
    "q12a"
    "q14a"
    "q15d"
    "q18c"
    "q19a"
    "q21a"
    "q22c"
    "q23a"
    "q24a"
    "q25b"
    "q26a"
    "q27a"
    "q28c"
    "q30c"
    "q31a"
    "q33c"
)

if [ ${benchmark_name} = "job" ]; then
    for bench in "${job_benchmarks[@]}"; do
        python3 ./benchmark/Benchmark.py ./benchmark/result-db/algorithm/job/${bench}_benchmark.yml -b build/release/ -o ./benchmark/result-db/algorithm/job/${bench}_results.csv
    done
else
    echo "The provided benchmark must be 'job', ${benchmark_name} was provided."
    exit 1
fi
