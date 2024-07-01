IMPORT INTO complete_cast DSV "benchmark/job/data/complete_cast.csv";
IMPORT INTO comp_cast_type DSV "benchmark/job/data/comp_cast_type.csv";
IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO company_type DSV "benchmark/job/data/company_type.csv";
IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO kind_type DSV "benchmark/job/data/kind_type.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO movie_info DSV "benchmark/job/data/movie_info.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	kt.kind,
	t.title
FROM
	complete_cast AS cc,
	comp_cast_type AS cct1,
	company_name AS cn,
	company_type AS ct,
	info_type AS it1,
	keyword AS k,
	kind_type AS kt,
	movie_companies AS mc,
	movie_info AS mi,
	movie_keyword AS mk,
	title AS t
WHERE
	cct1.kind = "complete+verified" AND
	cn.country_code = "[us]" AND
	it1.info = "release dates" AND
	(k.keyword = "nerd" OR k.keyword = "loner" OR k.keyword = "alienation" OR k.keyword = "dignity") AND
	(kt.kind = "movie") AND
	mi.note LIKE "%internet%" AND
	mi.info LIKE "USA:% 200%" AND
	t.production_year > 2000 AND
	kt.id = t.kind_id AND
	t.id = mi.movie_id AND
	t.id = mk.movie_id AND
	t.id = mc.movie_id AND
	t.id = cc.movie_id AND
	mk.movie_id = mi.movie_id AND
	mk.movie_id = mc.movie_id AND
	mk.movie_id = cc.movie_id AND
	mi.movie_id = mc.movie_id AND
	mi.movie_id = cc.movie_id AND
	mc.movie_id = cc.movie_id AND
	k.id = mk.keyword_id AND
	it1.id = mi.info_type_id AND
	cn.id = mc.company_id AND
	ct.id = mc.company_type_id AND
	cct1.id = cc.status_id;