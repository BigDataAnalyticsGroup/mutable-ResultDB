IMPORT INTO company_name DSV "benchmark/job/data/company_name.csv";
IMPORT INTO company_type DSV "benchmark/job/data/company_type.csv";
IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO movie_companies DSV "benchmark/job/data/movie_companies.csv";
IMPORT INTO movie_info DSV "benchmark/job/data/movie_info.csv";
IMPORT INTO movie_info_idx DSV "benchmark/job/data/movie_info_idx.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	mi.info,
	t.title
FROM
	company_name AS cn,
	company_type AS ct,
	info_type AS it1,
	info_type AS it2,
	movie_companies AS mc,
	movie_info AS mi,
	movie_info_idx AS mi_idx,
	title AS t
WHERE
	cn.country_code ="[us]" AND
	NOT ISNULL(ct.kind) AND
	(ct.kind ="production companies" OR ct.kind = "distributors") AND
	it1.info ="budget" AND
	it2.info ="bottom 10 rank" AND
	t.production_year >2000 AND
	(t.title LIKE "Birdemic%" OR t.title LIKE "%Movie%") AND
	t.id = mi.movie_id AND
	t.id = mi_idx.movie_id AND
	mi.info_type_id = it1.id AND
	mi_idx.info_type_id = it2.id AND
	t.id = mc.movie_id AND
	ct.id = mc.company_type_id AND
	cn.id = mc.company_id AND
	mc.movie_id = mi.movie_id AND
	mc.movie_id = mi_idx.movie_id AND
	mi.movie_id = mi_idx.movie_id;