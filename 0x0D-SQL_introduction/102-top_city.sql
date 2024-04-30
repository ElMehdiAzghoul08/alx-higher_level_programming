-- a script that displays the top 3 of ctz_ temperature during July and August ordered by temperature (descending)
SELECT x, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY x
ORDER BY avg_temp DESC
LIMIT 3;

