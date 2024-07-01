#!/usr/bin/env bash

if [ $# -eq 0 ]
  then
    echo "Provide which benchmarks to execute, currently only 'job' supported."
    exit 1
fi

benchmark_name="$1"

job_benchmarks=(
    "q1a"
    "q3b"
    "q4a"
    "q5b"
)

if [ ${benchmark_name} = "job" ]; then
    for bench in "${job_benchmarks[@]}"; do
        python3 ./benchmark/Benchmark.py ./benchmark/result-db/algorithm/job/${bench}_benchmark.yml -b build/release/ -o ./benchmark/result-db/algorithm/job/${bench}_results.csv
    done
else
    echo "The provided benchmark must be 'job', ${benchmark_name} was provided."
    exit 1
fi
