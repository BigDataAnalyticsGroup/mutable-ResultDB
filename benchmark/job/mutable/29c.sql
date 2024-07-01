IMPORT INTO aka_name DSV "benchmark/job/data/aka_name.csv";
IMPORT INTO complete_cast DSV "benchmark/job/data/complete_cast.csv";
IMPORT INTO comp_cast_type DSV "benchmark/job/data/comp_cast_type.csv";
IMPORT INTO char_name DSV "benchmark/job/data/char_name.csv";
IMPORT INTO cast_info DSV "benchmark/job/data/cast_info.csv";
IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO movie_info DSV "benchmark/job/data/movie_info.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO name DSV "benchmark/job/data/name.csv";
IMPORT INTO person_info DSV "benchmark/job/data/person_info.csv";
IMPORT INTO role_type DSV "benchmark/job/data/role_type.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	chn.name,
	n.name,
	t.title
FROM
	aka_name AS an,
	complete_cast AS cc,
	comp_cast_type AS cct1,
	comp_cast_type AS cct2,
	char_name AS chn,
	cast_info AS ci,
	company_name AS cn,
	info_type AS it,
	info_type AS it3,
	keyword AS k,
	movie_companies AS mc,
	movie_info AS mi,
	movie_keyword AS mk,
	name AS n,
	person_info AS pi,
	role_type AS rt,
	title AS t
WHERE
	cct1.kind ="cast" AND
	cct2.kind ="complete+verified" AND
	(ci.note = "(voice)" OR ci.note = "(voice: Japanese version)" OR ci.note = "(voice) (uncredited)" OR ci.note = "(voice: English version)") AND
	cn.country_code ="[us]" AND
	it.info = "release dates" AND
	it3.info = "trivia" AND
	k.keyword = "computer-animation" AND
	NOT ISNULL(mi.info) AND
	(mi.info LIKE "Japan:%200%" OR mi.info LIKE "USA:%200%") AND
	n.gender ="f" AND
	n.name LIKE "%An%" AND
	rt.role ="actress" AND
	t.production_year >= 2000 AND
	t.production_year <= 2010 AND
	t.id = mi.movie_id AND
	t.id = mc.movie_id AND
	t.id = ci.movie_id AND
	t.id = mk.movie_id AND
	t.id = cc.movie_id AND
	mc.movie_id = ci.movie_id AND
	mc.movie_id = mi.movie_id AND
	mc.movie_id = mk.movie_id AND
	mc.movie_id = cc.movie_id AND
	mi.movie_id = ci.movie_id AND
	mi.movie_id = mk.movie_id AND
	mi.movie_id = cc.movie_id AND
	ci.movie_id = mk.movie_id AND
	ci.movie_id = cc.movie_id AND
	mk.movie_id = cc.movie_id AND
	cn.id = mc.company_id AND
	it.id = mi.info_type_id AND
	n.id = ci.person_id AND
	rt.id = ci.role_id AND
	n.id = an.person_id AND
	ci.person_id = an.person_id AND
	chn.id = ci.person_role_id AND
	n.id = pi.person_id AND
	ci.person_id = pi.person_id AND
	it3.id = pi.info_type_id AND
	k.id = mk.keyword_id AND
	cct1.id = cc.subject_id AND
	cct2.id = cc.status_id;