-- a script that prepares a MySQL server for the project
-- DataBase hbnb_dev_db
-- new user hbnb_dev
-- Password hbnb_dev_db
-- hbnb_dev has all privileges on the database hbnb_dev_db
-- and has only select in db performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
