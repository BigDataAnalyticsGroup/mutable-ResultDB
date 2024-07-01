IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO company_type DSV "benchmark/job/data/company_type.csv";
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO link_type DSV "benchmark/job/data/link_type.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO movie_info DSV "benchmark/job/data/movie_info.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO movie_link DSV "benchmark/job/data/movie_link.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	cn.name,
	lt.link,
	t.title
FROM
	company_name AS cn,
	company_type AS ct,
	keyword AS k,
	link_type AS lt,
	movie_companies AS mc,
	movie_info AS mi,
	movie_keyword AS mk,
	movie_link AS ml,
	title AS t
WHERE
	cn.country_code !="[pl]" AND
	(cn.name LIKE "%Film%" OR cn.name LIKE "%Warner%") AND
	ct.kind ="production companies" AND
	k.keyword ="sequel" AND
	lt.link LIKE "%follow%" AND
	ISNULL(mc.note) AND
	(mi.info = "Sweden" OR mi.info = "Norway" OR mi.info = "Germany" OR mi.info = "Denmark" OR mi.info = "Swedish" OR mi.info = "Denish" OR mi.info = "Norwegian" OR mi.info = "German" OR mi.info = "English") AND
	t.production_year >= 1950 AND
	t.production_year <= 2010 AND
	lt.id = ml.link_type_id AND
	ml.movie_id = t.id AND
	t.id = mk.movie_id AND
	mk.keyword_id = k.id AND
	t.id = mc.movie_id AND
	mc.company_type_id = ct.id AND
	mc.company_id = cn.id AND
	mi.movie_id = t.id AND
	ml.movie_id = mk.movie_id AND
	ml.movie_id = mc.movie_id AND
	mk.movie_id = mc.movie_id AND
	ml.movie_id = mi.movie_id AND
	mk.movie_id = mi.movie_id AND
	mc.movie_id = mi.movie_id;