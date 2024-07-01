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
	(ci.note = "(producer)" OR ci.note = "(executive producer)") AND
	it1.info = "budget" AND
	it2.info = "votes" AND
	n.gender = "m" AND
	n.name LIKE "%Tim%" AND
	t.id = mi.movie_id AND
	t.id = mi_idx.movie_id AND
	t.id = ci.movie_id AND
	ci.movie_id = mi.movie_id AND
	ci.movie_id = mi_idx.movie_id AND
	mi.movie_id = mi_idx.movie_id AND
	n.id = ci.person_id AND
	it1.id = mi.info_type_id AND
	it2.id = mi_idx.info_type_id;