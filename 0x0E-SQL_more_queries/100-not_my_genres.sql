-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show DexterS
SELECT DISTINCT `tv_genres`.`name`
FROM `tv_show_genres`
INNER JOIN `tv_genres`
	ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
WHERE `tv_show_genres`.`show_id` != (
	SELECT `tv_shows`.`id`
	FROM `tv_shows`
	WHERE `tv_shows`.`title` = 'Dexter')
ORDER BY `tv_genres`.`name`;
