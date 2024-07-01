IMPORT INTO complete_cast DSV "benchmark/job/data/complete_cast.csv";
IMPORT INTO comp_cast_type DSV "benchmark/job/data/comp_cast_type.csv";
IMPORT INTO cast_info DSV "benchmark/job/data/cast_info.csv";
IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO movie_info DSV "benchmark/job/data/movie_info.csv";
IMPORT INTO movie_info_idx DSV "benchmark/job/data/movie_info_idx.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO name DSV "benchmark/job/data/name.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	mi.info,
	mi_idx.info,
	n.name,
	t.title
FROM
	complete_cast AS cc,
	comp_cast_type AS cct1,
	comp_cast_type AS cct2,
	cast_info AS ci,
	info_type AS it1,
	info_type AS it2,
	keyword AS k,
	movie_info AS mi,
	movie_info_idx AS mi_idx,
	movie_keyword AS mk,
	name AS n,
	title AS t
WHERE
	(cct1.kind = "cast" OR cct1.kind = "crew") AND
	cct2.kind ="complete+verified" AND
	(ci.note = "(writer)" OR ci.note = "(head writer)" OR ci.note = "(written by)" OR ci.note = "(story)" OR ci.note = "(story editor)") AND
	it1.info = "genres" AND
	it2.info = "votes" AND
	(k.keyword = "murder" OR k.keyword = "violence" OR k.keyword = "blood" OR k.keyword = "gore" OR k.keyword = "death" OR k.keyword = "female-nudity" OR k.keyword = "hospital") AND
	(mi.info = "Horror" OR mi.info = "Thriller") AND
	n.gender = "m" AND
	t.production_year > 2000 AND
	t.id = mi.movie_id AND
	t.id = mi_idx.movie_id AND
	t.id = ci.movie_id AND
	t.id = mk.movie_id AND
	t.id = cc.movie_id AND
	ci.movie_id = mi.movie_id AND
	ci.movie_id = mi_idx.movie_id AND
	ci.movie_id = mk.movie_id AND
	ci.movie_id = cc.movie_id AND
	mi.movie_id = mi_idx.movie_id AND
	mi.movie_id = mk.movie_id AND
	mi.movie_id = cc.movie_id AND
	mi_idx.movie_id = mk.movie_id AND
	mi_idx.movie_id = cc.movie_id AND
	mk.movie_id = cc.movie_id AND
	n.id = ci.person_id AND
	it1.id = mi.info_type_id AND
	it2.id = mi_idx.info_type_id AND
	k.id = mk.keyword_id AND
	cct1.id = cc.subject_id AND
	cct2.id = cc.status_id;