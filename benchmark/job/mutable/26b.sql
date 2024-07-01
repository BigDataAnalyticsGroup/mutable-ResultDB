IMPORT INTO complete_cast DSV "benchmark/job/data/complete_cast.csv";
IMPORT INTO comp_cast_type DSV "benchmark/job/data/comp_cast_type.csv";
IMPORT INTO char_name DSV "benchmark/job/data/char_name.csv";
IMPORT INTO cast_info DSV "benchmark/job/data/cast_info.csv";
IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO kind_type DSV "benchmark/job/data/kind_type.csv";
IMPORT INTO movie_info_idx DSV "benchmark/job/data/movie_info_idx.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO name DSV "benchmark/job/data/name.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	chn.name,
	mi_idx.info,
	t.title
FROM
	complete_cast AS cc,
	comp_cast_type AS cct1,
	comp_cast_type AS cct2,
	char_name AS chn,
	cast_info AS ci,
	info_type AS it2,
	keyword AS k,
	kind_type AS kt,
	movie_info_idx AS mi_idx,
	movie_keyword AS mk,
	name AS n,
	title AS t
WHERE
	cct1.kind = "cast" AND
	cct2.kind LIKE "%complete%" AND
	NOT ISNULL(chn.name) AND
	(chn.name LIKE "%man%" OR chn.name LIKE "%Man%") AND
	it2.info = "rating" AND
	(k.keyword = "superhero" OR k.keyword = "marvel-comics" OR k.keyword = "based-on-comic" OR k.keyword = "fight") AND
	kt.kind = "movie" AND
	mi_idx.info > "8.0" AND
	t.production_year > 2005 AND
	kt.id = t.kind_id AND
	t.id = mk.movie_id AND
	t.id = ci.movie_id AND
	t.id = cc.movie_id AND
	t.id = mi_idx.movie_id AND
	mk.movie_id = ci.movie_id AND
	mk.movie_id = cc.movie_id AND
	mk.movie_id = mi_idx.movie_id AND
	ci.movie_id = cc.movie_id AND
	ci.movie_id = mi_idx.movie_id AND
	cc.movie_id = mi_idx.movie_id AND
	chn.id = ci.person_role_id AND
	n.id = ci.person_id AND
	k.id = mk.keyword_id AND
	cct1.id = cc.subject_id AND
	cct2.id = cc.status_id AND
	it2.id = mi_idx.info_type_id;