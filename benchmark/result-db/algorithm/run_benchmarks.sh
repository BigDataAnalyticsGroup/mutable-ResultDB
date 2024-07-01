#!/usr/bin/env bash

if [ $# -eq 0 ]
  then
    echo "Provide which benchmarks to execute, either 'job' or 'star'."
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

star_benchmarks=(
    "star_sel_10"
    "star_sel_20"
    "star_sel_30"
    "star_sel_40"
    "star_sel_50"
    "star_sel_60"
    "star_sel_70"
    "star_sel_80"
    "star_sel_90"
    "star_sel_100"
)

if [ ${benchmark_name} = "job" ]; then
    for bench in "${job_benchmarks[@]}"; do
        python3 ./benchmark/Benchmark.py ./benchmark/result-db/algorithm/job/${bench}_benchmark.yml -b build/release/ -o ./benchmark/result-db/algorithm/job/${bench}_results.csv
    done
elif [ ${benchmark_name} = "star" ]; then
    for bench in "${star_benchmarks[@]}"; do
        python3 ./benchmark/Benchmark.py ./benchmark/result-db/algorithm/star/${bench}_benchmark.yml -b ./build/release/ -o ./benchmark/result-db/algorithm/star/${bench}_results.csv
    done
else
    echo "The provided benchmark must either be 'job' or 'star', ${benchmark_name} was provided."
    exit 1
fi
