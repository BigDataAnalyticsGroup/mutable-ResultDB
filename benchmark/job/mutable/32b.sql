IMPORT INTO keyword DSV "benchmark/job/data/keyword.csv";
IMPORT INTO link_type DSV "benchmark/job/data/link_type.csv";
IMPORT INTO movie_keyword DSV "benchmark/job/data/movie_keyword.csv";
IMPORT INTO movie_link DSV "benchmark/job/data/movie_link.csv";
IMPORT INTO title DSV "benchmark/job/data/title.csv";

SELECT
	lt.link,
	t1.title,
	t2.title
FROM
	keyword AS k,
	link_type AS lt,
	movie_keyword AS mk,
	movie_link AS ml,
	title AS t1,
	title AS t2
WHERE
	k.keyword ="character-name-in-title" AND
	mk.keyword_id = k.id AND
	t1.id = mk.movie_id AND
	ml.movie_id = t1.id AND
	ml.linked_movie_id = t2.id AND
	lt.id = ml.link_type_id AND
	mk.movie_id = t1.id;