-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT name
from tv_genres AS tg
INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
        INNER JOIN tv_shows AS ts
        ON tsg.show_id = ts.id
        WHERE tg.name NOT IN(
                SELECT name
                FROM tv_genre AS tg
                INNER JOIN tv_show_genres as tsg
                ON tg.id = tsg.genres
                
                INNER JOIN tv_shows AS ts
		ON tsg.show_id = t.id
		WHERE ts.title = "Dexter")
ORDER BY tg.name;
