IMPORT INTO aka_name DSV "benchmark/job/data/aka_name.csv";
IMPORT INTO cast_info DSV "benchmark/job/data/cast_info.csv";
IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO name DSV "benchmark/job/data/name.csv";
IMPORT INTO role_type DSV "benchmark/job/data/role_type.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	an.name,
	t.title
FROM
	aka_name AS an,
	cast_info AS ci,
	company_name AS cn,
	movie_companies AS mc,
	name AS n,
	role_type AS rt,
	title AS t
WHERE
	ci.note ="(voice: English version)" AND
	cn.country_code ="[jp]" AND
	mc.note LIKE "%(Japan)%" AND
	NOT mc.note LIKE "%(USA)%" AND
	(mc.note LIKE "%(2006)%" OR mc.note LIKE "%(2007)%") AND
	n.name LIKE "%Yo%" AND
	NOT n.name LIKE "%Yu%" AND
	rt.role ="actress" AND
	t.production_year >= 2006 AND
	t.production_year <= 2007 AND
	(t.title LIKE "One Piece%" OR t.title LIKE "Dragon Ball Z%") AND
	an.person_id = n.id AND
	n.id = ci.person_id AND
	ci.movie_id = t.id AND
	t.id = mc.movie_id AND
	mc.company_id = cn.id AND
	ci.role_id = rt.id AND
	an.person_id = ci.person_id AND
	ci.movie_id = mc.movie_id;