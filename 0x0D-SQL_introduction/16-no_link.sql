-- a script which list all studnts excluding null name values
SELECT score,name FROM second_table WHERE name IS NOT NULL ORDER BY 1 DESC;
