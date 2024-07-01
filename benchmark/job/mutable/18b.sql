IMPORT INTO cast_info DSV "benchmark/job/data/cast_info.csv";
IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO movie_info DSV "benchmark/job/data/movie_info.csv";
IMPORT INTO movie_info_idx DSV "benchmark/job/data/movie_info_idx.csv";
IMPORT INTO name DSV "benchmark/job/data/name.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	mi.info,
	mi_idx.info,
	t.title
FROM
	cast_info AS ci,
	info_type AS it1,
	info_type AS it2,
	movie_info AS mi,
	movie_info_idx AS mi_idx,
	name AS n,
	title AS t
WHERE
	(ci.note = "(writer)" OR ci.note = "(head writer)" OR ci.note = "(written by)" OR ci.note = "(story)" OR ci.note = "(story editor)") AND
	it1.info = "genres" AND
	it2.info = "rating" AND
	(mi.info = "Horror" OR mi.info = "Thriller") AND
	ISNULL(mi.note) AND
	mi_idx.info > "8.0" AND
	NOT ISNULL(n.gender) AND
	n.gender = "f" AND
	t.production_year >= 2008 AND
	t.production_year <= 2014 AND
	t.id = mi.movie_id AND
	t.id = mi_idx.movie_id AND
	t.id = ci.movie_id AND
	ci.movie_id = mi.movie_id AND
	ci.movie_id = mi_idx.movie_id AND
	mi.movie_id = mi_idx.movie_id AND
	n.id = ci.person_id AND
	it1.id = mi.info_type_id AND
	it2.id = mi_idx.info_type_id;