--  a script which compute average temprature by city and order by temp desc
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY 2 DESC;
