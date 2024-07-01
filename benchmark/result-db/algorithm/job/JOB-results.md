# JOB Query Results

* q1:
    * 1a :x: :arrow_right: Decompose introduces some duplicate rows where one attribute is `NULL`
    * 1b :white_check_mark:
    * 1c :white_check_mark:
    * 1d :white_check_mark:
* q2:
    * 2a :white_check_mark:
    * 2b :white_check_mark:
    * 2c :white_check_mark:
    * 2d :white_check_mark:
* q3:
    * 3a :white_check_mark:
    * 3b :white_check_mark:
    * 3c :white_check_mark:
* q4:
    * 4a :white_check_mark:
    * 4b :white_check_mark:
    * 4c :white_check_mark:
* q5:
    * 5a :white_check_mark:
    * 5b :white_check_mark:
    * 5c :white_check_mark:
* q6: :x: :arrow_right: ResultDB exhausts memory
* q7: :warning: Conduct experiments again
    * 7a :x:
    * 7b :white_check_mark:
    * 7c :x:
* q8:
    * 8a :white_check_mark: (empty result set)
    * 8b :white_check_mark: (empty result set)
    * 8c :x: :arrow_right: ResultDB and Decompose produce too few tuples (projection on `aka_name`)
    * 8d :x: :arrow_right: ResultDB and Decompose produce too few tuples (projection on `aka_name`)
* q9:
    * 9a :white_check_mark:
    * 9b :white_check_mark:
    * 9c :white_check_mark:
    * 9d :x: :arrow_right: ResultDB and Decompose produce one tuple less
* q10:
    * 10a: :white_check_mark:
    * 10b: :white_check_mark:
    * 10c: :white_check_mark:
* q11:
    * 11a: :white_check_mark:
    * 11b: :white_check_mark:
    * 11c: :white_check_mark:
    * 11d: :white_check_mark:
* q12:
    * 12a: :white_check_mark:
    * 12b: :x: :arrow_right: ResultDB exhausts memory (return code 9)
    * 12c: :white_check_mark:
* q13:
    * 13a: :x: :arrow_right: ResultDB exhausts memory
    * 13b: :x: :arrow_right: ResultDB exhausts memory
    * 13c: :x: :arrow_right: ResultDB exhausts memory
    * 13d: :x: :arrow_right: ResultDB exhausts memory
* q14:
    * 14a: :white_check_mark:
    * 14b: :white_check_mark:
    * 14c: :white_check_mark:
* q15:
    * 15a: :white_check_mark:
    * 15b: :white_check_mark:
    * 15c: :white_check_mark:
    * 15d: :white_check_mark:
* q16:
    * 16a: :x: :arrow_right: ResultDB exhausts memory
    * 16b: :x: :arrow_right: ResultDB exhausts memory
    * 16c: :x: :arrow_right: ResultDB exhausts memory
    * 16d: :x: :arrow_right: ResultDB exhausts memory
* q17:
    * 17a: :x: :arrow_right: ResultDB exhausts memory
    * 17b: :x: :arrow_right: ResultDB exhausts memory
    * 17c: :x: :arrow_right: ResultDB exhausts memory
    * 17d: :x: :arrow_right: ResultDB exhausts memory
    * 17e: :x: :arrow_right: ResultDB exhausts memory
    * 17f: :x: :arrow_right: ResultDB exhausts memory

* q18:
    * 18a: :white_check_mark:
    * 18b: :white_check_mark:
    * 18c: :white_check_mark:
* q19:
    * 19a: :white_check_mark:
    * 19b: :white_check_mark:
    * 19c: :white_check_mark:
    * 19d: :x: :arrow_right: ResultDB exhausts memory
* q20:
    * 20a: :x: :arrow_right: ResultDB exhausts memory
    * 20b: :x: :arrow_right: ResultDB exhausts memory
    * 20c: :x: :arrow_right: ResultDB exhausts memory
* q21:
    * 21a: :white_check_mark:
    * 21b: :white_check_mark:
    * 21c: :white_check_mark:
* q22:
    * 22a: :white_check_mark:
    * 22b: :white_check_mark:
    * 22c: :white_check_mark:
    * 22d: :x: :arrow_right: ResultDB exhausts memory
* q23:
    * 23a: :white_check_mark:
    * 23b: :white_check_mark:
    * 23c: :white_check_mark:
* q24:
    * 24a: :white_check_mark:
    * 24b: :white_check_mark:
* q25:
    * 25a: :white_check_mark:
    * 25b: :white_check_mark:
    * 25c: :white_check_mark:
* q26:
    * 26a: :white_check_mark:
    * 26b: :white_check_mark:
    * 26c: :x: :arrow_right: ResultDB exhausts memory
* q27:
    * 27a: :white_check_mark:
    * 27b: :white_check_mark:
    * 27c: :white_check_mark:
* q28:
    * 28a: :white_check_mark:
    * 28b: :white_check_mark:
    * 28c: :white_check_mark:
* q29: :warning: TODO
    * 29a: :x: :arrow_right: Single Table produces a wrong amount of result tuples; Cardinality has to be generated
    * 29b: :x: :arrow_right: Cardinality has to be generated
    * 29c: :x: :arrow_right: Cardinality has to be generated
* q30:
    * 30a: :white_check_mark:
    * 30b: :white_check_mark:
    * 30c: :white_check_mark:
* q31:
    * 31a: :white_check_mark:
    * 31b: :white_check_mark:
    * 31c: :x: :arrow_right: ResultDB exhausts memory
* q32:
    * 32a: :x: :arrow_right: ResultDB std::bad_alloc
    * 32b: :x: :arrow_right: ResultDB std::bad_alloc
* q33:
    * 33a: :white_check_mark:
    * 33b: :white_check_mark:
    * 33c: :white_check_mark:
