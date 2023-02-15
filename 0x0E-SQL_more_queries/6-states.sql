-- Creating a database hbtn_0d_usa
-- creating a table states with primary key 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256));

