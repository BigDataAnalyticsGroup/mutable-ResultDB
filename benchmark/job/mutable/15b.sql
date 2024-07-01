IMPORT INTO aka_title DSV "benchmark/job/data/aka_title.csv";
IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO company_type DSV "benchmark/job/data/company_type.csv";
IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO movie_info DSV "benchmark/job/data/movie_info.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	mi.info,
	t.title
FROM
	aka_title AS at,
	company_name AS cn,
	company_type AS ct,
	info_type AS it1,
	keyword AS k,
	movie_companies AS mc,
	movie_info AS mi,
	movie_keyword AS mk,
	title AS t
WHERE
	cn.country_code = "[us]" AND
	cn.name = "YouTube" AND
	it1.info = "release dates" AND
	mc.note LIKE "%(200%)%" AND
	mc.note LIKE "%(worldwide)%" AND
	mi.note LIKE "%internet%" AND
	mi.info LIKE "USA:% 200%" AND
	t.production_year >= 2005 AND
	t.production_year <= 2010 AND
	t.id = at.movie_id AND
	t.id = mi.movie_id AND
	t.id = mk.movie_id AND
	t.id = mc.movie_id AND
	mk.movie_id = mi.movie_id AND
	mk.movie_id = mc.movie_id AND
	mk.movie_id = at.movie_id AND
	mi.movie_id = mc.movie_id AND
	mi.movie_id = at.movie_id AND
	mc.movie_id = at.movie_id AND
	k.id = mk.keyword_id AND
	it1.id = mi.info_type_id AND
	cn.id = mc.company_id AND
	ct.id = mc.company_type_id;
