-- creating a database hbtn_0d_usa should not fail if exists
-- creating table cities in hbtn_0d_usa
-- Fields
--	id:INT
--	state_id: foreign key
--	name: varchar(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));

