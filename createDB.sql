CREATE DATABASE IF NOT EXISTS testDB;
USE testDB;
CREATE TABLE IF NOT EXISTS testTable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1 VARCHAR(50),
    column2 VARCHAR(50)
);
INSERT INTO testTable (column1, column2)
VALUES 
("test val 1", "test val 2"),
("test val 3", "test val 4"),
("test val 5", "test val 6"),
("test val 7", "test val 8"),
("test val 9", "test val 10");
SELECT * FROM testTable;