CREATE DATABASE result_db;
USE result_db;

CREATE TABLE fact (
    id INT(4) NOT NULL,
    fkd1 INT(4) NOT NULL,
    fkd2 INT(4) NOT NULL,
    fkd3 INT(4) NOT NULL,
    fkd4 INT(4) NOT NULL,
    a INT(4) NOT NULL,
    b CHAR(16) NOT NULL
);

CREATE TABLE dim1 (
    id INT(4) NOT NULL,
    a INT(4) NOT NULL,
    b CHAR(16) NOT NULL
);

CREATE TABLE dim2 (
    id INT(4) NOT NULL,
    a INT(4) NOT NULL,
    b CHAR(16) NOT NULL
);

CREATE TABLE dim3 (
    id INT(4) NOT NULL,
    a INT(4) NOT NULL,
    b CHAR(16) NOT NULL
);

CREATE TABLE dim4 (
    id INT(4) NOT NULL,
    a INT(4) NOT NULL,
    b CHAR(16) NOT NULL
);


-- IMPORT DATA --
IMPORT INTO fact DSV "benchmark/result-db/star-schema/data/fact.csv";
IMPORT INTO dim1 DSV "benchmark/result-db/star-schema/data/dim1.csv";
IMPORT INTO dim2 DSV "benchmark/result-db/star-schema/data/dim2.csv";
IMPORT INTO dim3 DSV "benchmark/result-db/star-schema/data/dim3.csv";
IMPORT INTO dim4 DSV "benchmark/result-db/star-schema/data/dim4.csv";
