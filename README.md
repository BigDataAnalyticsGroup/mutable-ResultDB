# Result DB
The folder **mutable_fork_resultdb** contains a **fork** of [mu*t*able](https://github.com/mutable-org/mutable) including the Result DB implementation.

## Result DB Experiments
To execute the Result DB experiments, please follow these
[instructions](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/README.md).

## Result DB Modifications and Contributions
The following files inside the **mutable_fork_resultdb** repository were _modified_:

* [include/mutable/IR/Operator.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/include/mutable/IR/Operator.hpp)
* [include/mutable/IR/Optimizer.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/include/mutable/IR/Optimizer.hpp)
* [include/mutable/IR/QueryGraph.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/include/mutable/IR/QueryGraph.hpp)
* [include/mutable/Options.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/include/mutable/Options.hpp)
* [include/mutable/backend/WebAssembly.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/include/mutable/backend/WebAssembly.hpp)
* [include/mutable/util/ADT.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/include/mutable/util/ADT.hpp)
* [include/mutable/util/AdjacencyMatrix.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/include/mutable/util/AdjacencyMatrix.hpp)
* [src/IR/Operator.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/IR/Operator.cpp)
* [src/IR/Optimizer.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/IR/Optimizer.cpp)
* [src/backend/Interpreter.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/Interpreter.cpp)
* [src/backend/V8Engine.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/V8Engine.cpp)
* [src/backend/V8Engine.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/V8Engine.hpp)
* [src/backend/WasmAlgo.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/WasmAlgo.cpp)
* [src/backend/WasmAlgo.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/WasmAlgo.hpp)
* [src/backend/WasmDSL.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/WasmDSL.cpp)
* [src/backend/WasmDSL.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/WasmDSL.hpp)
* [src/backend/WasmOperator.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/WasmOperator.cpp)
* [src/backend/WasmOperator.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/WasmOperator.hpp)
* [src/backend/WasmUtil.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/WasmUtil.cpp)
* [src/backend/WasmUtil.hpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/WasmUtil.hpp)
* [src/backend/WebAssembly.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/backend/WebAssembly.cpp)
* [src/catalog/DatabaseCommand.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/catalog/DatabaseCommand.cpp)
* [src/shell.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/shell.cpp)
* [src/util/AdjacencyMatrix.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/src/util/AdjacencyMatrix.cpp)
* [test/IntegrationTest.py](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/test/IntegrationTest.py)
* [unittest/backend/WasmDSLTest.tpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/unittest/backend/WasmDSLTest.tpp)
* [unittest/backend/WasmOperatorTest.tpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/unittest/backend/WasmOperatorTest.tpp)
* [unittest/backend/WasmTestV8.cpp](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/unittest/backend/WasmTestV8.cpp)

The following folder and files inside the **mutable_fork_resultdb** repository were _added_:

* [test/ours/end2end-result-db-chain_2.yml](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/test/ours/end2end-result-db-chain_2.yml)
* [test/ours/end2end-result-db-cycle_3.yml](https://github.com/BigDataAnalyticsGroup/mutable-ResultDB/blob/resultdb-submission/mutable_fork_resultdb/test/ours/end2end-result-db-cycle_3.yml)
* test/result-db/ (all files in this folder)
* benchmark/result-db/ (all files in this folder)
