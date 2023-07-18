-- script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
SELECT city, AVG(VALUE) AS avg_temp
FROM temperature
WHERE month IN (July, August)
GROUP BY city
ORDER BY avg_temp DESC;
