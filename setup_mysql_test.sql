-- a script that prepares a MySQL server for the project
-- DataBase hbnb_dev_db
-- new user hbnb_dev
-- Password hbnb_dev_db
-- hbnb_dev has all privileges on the database hbnb_dev_db
-- and has only select in db performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
