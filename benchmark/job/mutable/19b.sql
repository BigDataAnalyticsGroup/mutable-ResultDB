IMPORT INTO aka_name DSV "benchmark/job/data/aka_name.csv";
IMPORT INTO char_name DSV "benchmark/job/data/char_name.csv";
IMPORT INTO cast_info DSV "benchmark/job/data/cast_info.csv";
IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO movie_info DSV "benchmark/job/data/movie_info.csv";
IMPORT INTO name DSV "benchmark/job/data/name.csv";
IMPORT INTO role_type DSV "benchmark/job/data/role_type.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	n.name,
	t.title
FROM
	aka_name AS an,
	char_name AS chn,
	cast_info AS ci,
	company_name AS cn,
	info_type AS it,
	movie_companies AS mc,
	movie_info AS mi,
	name AS n,
	role_type AS rt,
	title AS t
WHERE
	ci.note = "(voice)" AND
	cn.country_code ="[us]" AND
	it.info = "release dates" AND
	mc.note LIKE "%(200%)%" AND
	(mc.note LIKE "%(USA)%" OR mc.note LIKE "%(worldwide)%") AND
	NOT ISNULL(mi.info) AND
	(mi.info LIKE "Japan:%2007%" OR mi.info LIKE "USA:%2008%") AND
	n.gender ="f" AND
	n.name LIKE "%Angel%" AND
	rt.role ="actress" AND
	t.production_year >= 2007 AND
	t.production_year <= 2008 AND
	t.title LIKE "%Kung%Fu%Panda%" AND
	t.id = mi.movie_id AND
	t.id = mc.movie_id AND
	t.id = ci.movie_id AND
	mc.movie_id = ci.movie_id AND
	mc.movie_id = mi.movie_id AND
	mi.movie_id = ci.movie_id AND
	cn.id = mc.company_id AND
	it.id = mi.info_type_id AND
	n.id = ci.person_id AND
	rt.id = ci.role_id AND
	n.id = an.person_id AND
	ci.person_id = an.person_id AND
	chn.id = ci.person_role_id;