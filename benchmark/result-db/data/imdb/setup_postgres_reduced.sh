#!/usr/bin/env bash

if [ $# -eq 0 ]
then
    echo "Supply PostgreSQL username."
    exit 1
fi

USER=$1
DB_NAME="imdb_reduced"

# Drop and create database
psql -U ${USER} -d postgres -c "DROP DATABASE IF EXISTS "${DB_NAME}
psql -U ${USER} -d postgres -c "CREATE DATABASE "${DB_NAME}

# Create tables
psql -U ${USER} -d ${DB_NAME} -f "$(pwd)/benchmark/result-db/data/imdb/schema_postgres.sql"

# Import data
psql -U ${USER} -d ${DB_NAME} -c "\copy aka_name FROM '$(pwd)/benchmark/job/data/aka_name.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy aka_title FROM '$(pwd)/benchmark/job/data/aka_title.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy cast_info FROM '$(pwd)/benchmark/job/data/cast_info.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy char_name FROM '$(pwd)/benchmark/job/data/char_name.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy comp_cast_type FROM '$(pwd)/benchmark/job/data/comp_cast_type.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy company_name FROM '$(pwd)/benchmark/job/data/company_name.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy company_type FROM '$(pwd)/benchmark/job/data/company_type.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy complete_cast FROM '$(pwd)/benchmark/job/data/complete_cast.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy info_type FROM '$(pwd)/benchmark/job/data/info_type.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy keyword FROM '$(pwd)/benchmark/job/data/keyword.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy kind_type FROM '$(pwd)/benchmark/job/data/kind_type.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy link_type FROM '$(pwd)/benchmark/job/data/link_type.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy movie_companies FROM '$(pwd)/benchmark/job/data/movie_companies.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy movie_info FROM '$(pwd)/benchmark/job/data/movie_info.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy movie_info_idx FROM '$(pwd)/benchmark/job/data/movie_info_idx.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy movie_keyword FROM '$(pwd)/benchmark/job/data/movie_keyword.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy movie_link FROM '$(pwd)/benchmark/job/data/movie_link.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy name FROM '$(pwd)/benchmark/job/data/name.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy person_info FROM '$(pwd)/benchmark/job/data/person_info.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy role_type FROM '$(pwd)/benchmark/job/data/role_type.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy title FROM '$(pwd)/benchmark/job/data/title.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";

# Trim data according to reduced mutable schema
psql -U ${USER} -d ${DB_NAME} -c "UPDATE aka_name SET name=LEFT(name,16)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE aka_name SET imdb_index=LEFT(imdb_index,3)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE aka_title SET title=LEFT(title,21)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE aka_title SET imdb_index=LEFT(imdb_index,4)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE aka_title SET note=LEFT(note,22)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE cast_info SET note=LEFT(note,18)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE char_name SET name=LEFT(name,100)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE char_name SET imdb_index=LEFT(imdb_index,2)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE company_name SET name=LEFT(name,100)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE company_name SET country_code=LEFT(country_code,6)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE keyword SET keyword=LEFT(keyword,74)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE movie_companies SET note=LEFT(note,100)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE movie_info SET info=LEFT(info,43)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE movie_info SET note=LEFT(note,19)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE movie_info_idx SET info=LEFT(info,3)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE movie_info_idx SET note=LEFT(note,1)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE name SET name=LEFT(name,100)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE name SET imdb_index=LEFT(imdb_index,9)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE person_info SET info=LEFT(info,1)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE person_info SET note=LEFT(note,1)";

psql -U ${USER} -d ${DB_NAME} -c "UPDATE title SET title=LEFT(title,100)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE title SET imdb_index=LEFT(imdb_index,5)";
psql -U ${USER} -d ${DB_NAME} -c "UPDATE title SET series_years=LEFT(series_years,9)";

# Create indexes
psql -U ${USER} -d ${DB_NAME} -f "$(pwd)/benchmark/result-db/data/imdb/fkindexes.sql"
