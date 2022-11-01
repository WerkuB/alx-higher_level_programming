--  a script which print top 3 cities by average temp in july and Aug
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7,8)
GROUP BY city ORDER BY 2 DESC LIMIT 3;
