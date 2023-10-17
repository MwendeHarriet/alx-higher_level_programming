-- script lists number of records with same score in database in MySQL server
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
