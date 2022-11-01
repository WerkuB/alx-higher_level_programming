-- a script which displays number of records with score
select score, count(*) as 'number' from second_table group by score order by 2 desc;
