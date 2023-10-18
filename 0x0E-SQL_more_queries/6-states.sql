-- script creates database hbtn_0d_usa and table states therein in the MySQL server
-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creates table
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256)
);
