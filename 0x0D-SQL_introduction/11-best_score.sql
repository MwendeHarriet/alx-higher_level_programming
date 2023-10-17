--  script lists records with a score >= 10 in 2nd table in database the MySQL server
SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
