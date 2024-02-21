-- install MySQL server for running
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
