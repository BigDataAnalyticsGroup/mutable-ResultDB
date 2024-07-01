IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO company_type DSV "benchmark/job/data/company_type.csv";
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO link_type DSV "benchmark/job/data/link_type.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO movie_link DSV "benchmark/job/data/movie_link.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	cn.name
FROM
	company_name AS cn,
	company_type AS ct,
	keyword AS k,
	link_type AS lt,
	movie_companies AS mc,
	movie_keyword AS mk,
	movie_link AS ml,
	title AS t
WHERE
	cn.country_code !="[pl]" AND
	(cn.name LIKE "20th Century Fox%" OR cn.name LIKE "Twentieth Century Fox%") AND
	ct.kind != "production companies" AND
	NOT ISNULL(ct.kind) AND
	(k.keyword = "sequel" OR k.keyword = "revenge" OR k.keyword = "based-on-novel") AND
	NOT ISNULL(mc.note) AND
	t.production_year > 1950 AND
	lt.id = ml.link_type_id AND
	ml.movie_id = t.id AND
	t.id = mk.movie_id AND
	mk.keyword_id = k.id AND
	t.id = mc.movie_id AND
	mc.company_type_id = ct.id AND
	mc.company_id = cn.id AND
	ml.movie_id = mk.movie_id AND
	ml.movie_id = mc.movie_id AND
	mk.movie_id = mc.movie_id;