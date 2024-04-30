--  a script that displays the max temperature of each x (ordered by State name).
SELECT x, max(value) as max_temp
FROM temperatures
GROUP BY x
ORDER BY x;

