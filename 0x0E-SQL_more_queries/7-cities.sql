-- script creates database hbtn_0d_usa and table cities therein in the MySQL server
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
