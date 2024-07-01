# Instructions
This page gives a step-by-step instruction on how to carry out the `Result DB` experiments.
All the following commands have to be executed from the root project folder!

## General Prerequisites
* Set up a Python virtual environment using [pipenv](https://pipenv.pypa.io/en/latest/).
    ```console
    $ pipenv sync
    ```
    This installs all required Python packages for the utility scripts and visualization.
    In case of problems with `pygraphviz` on macOS, check this [doc](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/main/doc/preliminaries.md#pipenv).

    ```console
    $ pipenv shell
    ```
    This spawns a shell within the virtual environment.

* Download IMDb dataset.
    ```console
    $ python ./benchmark/get_data.py job
    ```
    This downloads the IMDb dataset to `./benchmark/job/data/`.

* Create synthetic star schema dataset.
    ```console
    $ python ./benchmark/result-db/data/synthetic-star-schema/generate_data.py
    ```
    This creates the synthetic star schema as described in the paper and stores the `csv` files in
    `./benchmark/result-db/data/synthetic-star-schema/`.

* Install and setup PostgreSQL.
    - Install [PostgreSQL](https://www.postgresql.org/) for your operating system. Note, that the experiments in the paper
    were conducted with PostgreSQL version 16.2.

    - Once installed, set the _shared\_buffers_ value to 16 GiB and _work\_mem_ to 1 GiB. There are multiple ways to [set parameters](https://www.postgresql.org/docs/current/config-setting.html).

        For the experiments, we changed the parameters via the configuration file `postgresql.conf`.
        The configuration file is usually contained in the database cluster's data directory, e.g. `/usr/local/var/postgresql/` on macOS Intel or `/var/lib/postgres/data/` on Linux.
        Make sure to restart your server after changing the values.

    - Create the databases and import the data.
        ```console
        $ ./benchmark/result-db/data/imdb/setup_postgres.sh <username>
        $ ./benchmark/result-db/data/synthetic-star-schema/setup_postgres.sh <username>
        ```

* Build mutable with the WebAssembly backend
    - Make sure to have all required [prerequisites](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/main/doc/preliminaries.md).
    - Setup mutable by following these
      [instructions](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/main/doc/setup.md#build-mutable).
      Note, that you have to build mutable with its WebAssembly-based backend.

## Result Set Sizes
The corresponding experiments can be found in `./result-set-sizes/`.
* Join Order Benchmark

    Execute the following script.
    ```console
    $ python ./benchmark/result-db/result-set-sizes/compute_result_set_size.py -u <username>
    ```
    This script creates `sql` files for each JOB query in `./benchmark/result-db/result-set-sizes/job/<query>`.
    Each file computes the number of result rows and the size of the required attributes for a specific relation.
    The SQL queries are executed using PostgreSQL and the results are written to
    `./benchmark/result-db/result-set-sizes/job/result-set-sizes.csv`.
* Synthetic Star Schema

    Since we exactly know how our results look like for different selectivity values, we do not have to manually
      compute the result sets. We can just calculate the result sets as done in the Visualization notebook.

## Rewrite Methods
* Join Order Benchmark
    - To generate the rewrite methods, execute the following script.
        ```console
        $ python ./benchmark/result-db/rewrite-methods/generate_rewrite_methods.py -q imdb -o benchmark/result-db/rewrite-methods/job/ --no-data-transfer
        ```
        This script creates `sql` files for each JOB query in `./benchmark/result-db/rewrite-methods/job/<query>`.
        Each file corresponds to either the default query or one of the rewrite methods.
    - Run each query using the following command. **Make sure to add your PostgreSQL username!**
        ```console
        $ python ./benchmark/result-db/rewrite-methods/run.py -u <username> -d imdb -n 5 -q imdb --directory ./benchmark/result-db/rewrite-methods/job/
        ```
    - The results can be found in `./benchmark/result-db/rewrite-methods/job/rewrite-results.csv`.
* Synthetic Star Schema
    - To generate the rewrite methods, execute the following script.
        ```console
        $ python ./benchmark/result-db/rewrite-methods/generate_rewrite_methods.py -q star -o benchmark/result-db/rewrite-methods/star/ --no-data-transfer
        ```
    - Run each query using the following command. **Make sure to add your PostgreSQL username!**
        ```console
        $ python ./benchmark/result-db/rewrite-methods/run.py -u <username> -d star -n 5 -q star --directory ./benchmark/result-db/rewrite-methods/star/
        ```
    - The results can be found in `./benchmark/result-db/rewrite-methods/star/rewrite-results.csv`.

## Result DB Algorithm
* Join Order Benchmark
    - Generate the real cardinalities for injection into mutable. **Make sure to add your PostgreSQL username!**
    ```console
    $ ./benchmark/result-db/algorithm/create_injected_cardinalities.py -u <username> -d imdb -q imdb -o ./benchmark/result-db/algorithm/job/
    ```
    - Run the benchmark scripts.
    ```console
    ./benchmark/result-db/algorithm/run_benchmarks.sh job
    ```
    - The results are individually written to `<query>_results.csv`.
* Synthetic Star Schema
    - Generate the real cardinalities for injection into mutable. **Make sure to add your PostgreSQL username!**
    ```console
    $ python ./benchmark/result-db/algorithm/create_injected_cardinalities.py -u <username> -d star -q star -o ./benchmark/result-db/algorithm/star/
    ```
    - Run the benchmark scripts.
    ```console
    ./benchmark/result-db/algorithm/run_benchmarks.sh star
    ```
    - The results are individually written to `./benchmark/result-db/algorithm/job/<query>_results.csv`.

## Post-join
* Join Order Benchmark
    - Generate the post-join files. This includes the reduced base tables, real cardinalities, benchmark script for
      execution in mutable, and (setup) files for the execution in PostgreSQL.
    ```console
    $ python ./benchmark/result-db/post-join/generate_post-join.py -u <username> -d imdb -q imdb -o ./benchmark/result-db/post-join/job/
    ```
    - Run the PostgreSQL benchmarks:
    ```console
    $ python ./benchmark/result-db/post-join/run_postgres.py -u <username> -d imdb -n 5 -q imdb --directory ./benchmark/result-db/post-join/job/
    ```
    - Run the mutable benchmarks:
    ```console
    $ python ./benchmark/result-db/post-join/run_mutable.py --workload job
    ```
    - The mutable results are written to `./benchmark/result-db/post-join/job/<query>/<query>_results.csv`. The
      PostgreSQL results are written to `./benchmark/result-db/post-join/job/postjoin-postgres-results.csv`.

## Visualization
All figures and data (i.e., result set sizes and overheads) presented in the paper can be found in the `Visualization.ipynb` notebook located in `./benchmark/result-db/visualization/`.
