-- script lists all records in the table where name is not null in database in MySQL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
