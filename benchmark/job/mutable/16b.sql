IMPORT INTO aka_name DSV "benchmark/job/data/aka_name.csv";
IMPORT INTO cast_info DSV "benchmark/job/data/cast_info.csv";
IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO name DSV "benchmark/job/data/name.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	an.name,
	t.title
FROM
	aka_name AS an,
	cast_info AS ci,
	company_name AS cn,
	keyword AS k,
	movie_companies AS mc,
	movie_keyword AS mk,
	name AS n,
	title AS t
WHERE
	cn.country_code ="[us]" AND
	k.keyword ="character-name-in-title" AND
	an.person_id = n.id AND
	n.id = ci.person_id AND
	ci.movie_id = t.id AND
	t.id = mk.movie_id AND
	mk.keyword_id = k.id AND
	t.id = mc.movie_id AND
	mc.company_id = cn.id AND
	an.person_id = ci.person_id AND
	ci.movie_id = mc.movie_id AND
	ci.movie_id = mk.movie_id AND
	mc.movie_id = mk.movie_id;