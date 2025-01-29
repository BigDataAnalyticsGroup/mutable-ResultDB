IMPORT INTO info_type DSV "benchmark/job/data/info_type.csv";
IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO kind_type DSV "benchmark/job/data/kind_type.csv";
IMPORT INTO movie_info DSV "benchmark/job/data/movie_info.csv";
IMPORT INTO movie_info_idx DSV "benchmark/job/data/movie_info_idx.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	mi_idx.info,
	t.title
FROM
	info_type AS it1,
	info_type AS it2,
	keyword AS k,
	kind_type AS kt,
	movie_info AS mi,
	movie_info_idx AS mi_idx,
	movie_keyword AS mk,
	title AS t
WHERE
	it1.info = "countries" AND
	it2.info = "rating" AND
	(k.keyword = "murder" OR k.keyword = "murder-in-title" OR k.keyword = "blood" OR k.keyword = "violence") AND
	kt.kind = "movie" AND
	(mi.info = "Sweden" OR mi.info = "Norway" OR mi.info = "Germany" OR mi.info = "Denmark" OR mi.info = "Swedish" OR mi.info = "Denish" OR mi.info = "Norwegian" OR mi.info = "German" OR mi.info = "USA" OR mi.info = "American") AND
	mi_idx.info < "8.5" AND
	t.production_year > 2010 AND
	kt.id = t.kind_id AND
	t.id = mi.movie_id AND
	t.id = mk.movie_id AND
	t.id = mi_idx.movie_id AND
	mk.movie_id = mi.movie_id AND
	mk.movie_id = mi_idx.movie_id AND
	mi.movie_id = mi_idx.movie_id AND
	k.id = mk.keyword_id AND
	it1.id = mi.info_type_id AND
	it2.id = mi_idx.info_type_id;