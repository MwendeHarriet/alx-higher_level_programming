-- script creates database hbtn_0d_usa and table cities therein in the MySQL server
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create tables
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES states(id)
)
