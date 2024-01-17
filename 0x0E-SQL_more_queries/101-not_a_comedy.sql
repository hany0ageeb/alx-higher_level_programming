-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT tv_shows.title AS "title"
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
OR tv_show_genres.genre_id <> (
	SELECT tv_genres.id
	FROM tv_genres
	WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title;
