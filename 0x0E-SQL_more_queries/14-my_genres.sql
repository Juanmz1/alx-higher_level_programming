-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT tg.`name`
  FROM `tv_genres` AS tg
       INNER JOIN `tv_show_genres` AS ts
       ON tg.`id` = ts.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON t.`id` = ts.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY tg.`name`;
