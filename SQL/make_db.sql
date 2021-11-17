CREATE DATABASE CGItest;
USE CGItest;


CREATE TABLE person (
	id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(50)
);

INSERT INTO person (first_name,last_name,phone) VALUES ("Simon","Andrews","1234");
INSERT INTO person (first_name,last_name,phone) VALUES ("James","Andrews","2345");
INSERT INTO person (first_name,last_name,phone) VALUES ("Frank","Andrews","3456");
INSERT INTO person (first_name,last_name,phone) VALUES ("Frank","Smith","4567");

CREATE USER cgiuser@localhost;
GRANT SELECT ON CGItest.* TO cgiuser@localhost;

FLUSH PRIVILEGES;
