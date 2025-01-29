IMPORT INTO aka_name DSV "benchmark/job/data/aka_name.csv";
IMPORT INTO char_name DSV "benchmark/job/data/char_name.csv";
IMPORT INTO cast_info DSV "benchmark/job/data/cast_info.csv";
IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO name DSV "benchmark/job/data/name.csv";
IMPORT INTO role_type DSV "benchmark/job/data/role_type.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	an.name,
	chn.name,
	n.name,
	t.title
FROM
	aka_name AS an,
	char_name AS chn,
	cast_info AS ci,
	company_name AS cn,
	movie_companies AS mc,
	name AS n,
	role_type AS rt,
	title AS t
WHERE
	(ci.note = "(voice)" OR ci.note = "(voice: Japanese version)" OR ci.note = "(voice) (uncredited)" OR ci.note = "(voice: English version)") AND
	cn.country_code ="[us]" AND
	n.gender ="f" AND
	n.name LIKE "%An%" AND
	rt.role ="actress" AND
	ci.movie_id = t.id AND
	t.id = mc.movie_id AND
	ci.movie_id = mc.movie_id AND
	mc.company_id = cn.id AND
	ci.role_id = rt.id AND
	n.id = ci.person_id AND
	chn.id = ci.person_role_id AND
	an.person_id = n.id AND
	an.person_id = ci.person_id;