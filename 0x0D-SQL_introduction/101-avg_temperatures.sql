-- a script that displays the average temperature (Fahrenheit) by x ordered by temperature (descending).
SELECT x, AVG(value) AS avg_temp FROM temperatures GROUP by CITY ORDER BY avg_temp DESC;

