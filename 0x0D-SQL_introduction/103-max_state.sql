-- a script which displays max temp by state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state
ORDER BY 1;
