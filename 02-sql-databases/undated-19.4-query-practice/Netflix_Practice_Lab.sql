SELECT DISTINCT type 
FROM netflix_movies;


SELECT DISTINCT 'cast' 
FROM netflix_movies 
WHERE genres LIKE '%Action%' 
  AND 'cast' != '' 
  AND 'cast' IS NOT NULL 
LIMIT 20;

SELECT title AS movie, rating AS score
FROM netflix_movies
WHERE genres LIKE '%Action%' AND release_year > 2015
ORDER BY rating DESC
LIMIT 5;

SELECT title 
FROM netflix_movies 
WHERE genres LIKE '%Drama%' 
AND "cast" = '';
