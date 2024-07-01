IMPORT INTO aka_name DSV "benchmark/job/data/aka_name.csv";
IMPORT INTO cast_info DSV "benchmark/job/data/cast_info.csv";
IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO link_type DSV "benchmark/job/data/link_type.csv";
IMPORT INTO movie_link DSV "benchmark/job/data/movie_link.csv";
IMPORT INTO name DSV "benchmark/job/data/name.csv";
IMPORT INTO person_info DSV "benchmark/job/data/person_info.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT n.name,
       pi.info
FROM aka_name AS an,
     cast_info AS ci,
     info_type AS it,
     link_type AS lt,
     movie_link AS ml,
     name AS n,
     person_info AS pi,
     title AS t
WHERE NOT ISNULL(an.name)
  AND (an.name LIKE "%a%"
       OR an.name LIKE "A%")
  AND it.info = "mini biography"
  AND (lt.link = "references" OR lt.link = "referenced in" OR lt.link = "features" OR lt.link = "featured in")
  AND n.name_pcode_cf >= "A"
  AND n.name_pcode_cf <= "F"
  AND (n.gender= "m"
       OR (n.gender = "f"
           AND n.name LIKE "A%"))
  AND NOT ISNULL(pi.note)
  AND t.production_year >= 1980
  AND t.production_year <= 2010
  AND n.id = an.person_id
  AND n.id = pi.person_id
  AND ci.person_id = n.id
  AND t.id = ci.movie_id
  AND ml.linked_movie_id = t.id
  AND lt.id = ml.link_type_id
  AND it.id = pi.info_type_id
  AND pi.person_id = an.person_id
  AND pi.person_id = ci.person_id
  AND an.person_id = ci.person_id
  AND ci.movie_id = ml.linked_movie_id;
