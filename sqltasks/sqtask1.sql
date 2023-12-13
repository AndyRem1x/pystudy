Database: testbase

DROP DATABASE IF EXISTS testbase;

CREATE DATABASE testbase
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

DROP TABLE IF EXISTS new_database;
DROP TABLE IF EXISTS Avengers;

CREATE TABLE IF NOT EXISTS new_database (
    id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	real_name TEXT NOT NULL
);

INSERT INTO new_database (name, real_name) VALUES 
	('Iron Man', 'Tony Stark'),
	('Captain America', 'Steve Rogers'),	
	('Hulk', 'Bruce Banner');
	
ALTER TABLE new_database RENAME TO Avengers;
ALTER TABLE Avengers ADD COLUMN actor text;	

UPDATE Avengers SET actor = 'Robert Downey Jr.' WHERE name = 'Iron Man';
UPDATE Avengers SET actor = 'Chris Evans' WHERE name = 'Captain America';
UPDATE Avengers SET actor = 'Mark Ruffalo' WHERE name = 'Hulk';


INSERT INTO Avengers (name, real_name, actor) VALUES 
	('Thor', '	Thor Odinson', 'Chris Hemsworth'),
	('Black Widow', 'Natasha Romanoff', 'Scarlett Johansson'),	
	('Quicksilver', 'Pietro Maximoff', 'Aaron Taylor-Johnson'),
	('Falcon', 'Samuel Wilson', 'Anthony Mackie'),
	('Hawkeye', 'Clint Barton', 'Jeremy Renner'),
	('Vision', 'Vision', 'Paul Bettany'),
	('Scarlet Witch', 'Wanda Maximoff', 'Elizabeth Olsen');

DELETE FROM Avengers WHERE real_name = 'Pietro Maximoff';
SELECT * FROM Avengers