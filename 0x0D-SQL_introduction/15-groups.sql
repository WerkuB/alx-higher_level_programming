-- a script which displays number of records with score
SELECT score, COUNT(*) AS 'number' FROM second_table GROUP BY score ORDER BY 2 DESC;
