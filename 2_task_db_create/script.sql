CREATE TABLE Product (
	maker varchar(255),
	model varchar(255) UNIQUE,
	"type" varchar(255)
);

INSERT INTO Product VALUES ('Asus', 'T90', 'PC');
INSERT INTO Product VALUES ('Asus', 'T91', 'PC');
INSERT INTO Product VALUES ('Acer', 'A22', 'Laptop');
INSERT INTO Product VALUES ('Apple', 'PRO', 'Laptop');
INSERT INTO Product VALUES ('Xerox', 'DL5564', 'Printer');
INSERT INTO Product VALUES ('Xerox', 'DX62', 'Printer');
INSERT INTO Product VALUES ('Canon', '2460', 'Printer');
INSERT INTO Product VALUES ('Samsung', 'XL', 'Printer');


CREATE TABLE PC (
	code integer PRIMARY KEY,
	model varchar(255) references Product(model),
	speed integer,
	ram integer,
	hd integer,
	cd varchar(4),
	price integer
);

INSERT INTO PC VALUES (0,'T90',4,12,120,'12x',450);
INSERT INTO PC VALUES (1,'T91',2,6,240,'24x',850);
INSERT INTO PC VALUES (2,'A22',4,24,540,'24x',1200);
INSERT INTO PC VALUES (3,'PRO',2,4,120,'24x',599);


CREATE TABLE Laptop (
	code integer PRIMARY KEY,
	model varchar(255) references Product(model),
	speed integer,
	ram integer,
	hd integer,
	screen integer,
	price integer
);

INSERT INTO Laptop VALUES (0,'T90',4,12,120,15,120);
INSERT INTO Laptop VALUES (1,'T91',2,6,240,17,750);
INSERT INTO Laptop VALUES (2,'A22',4,24,540,21,1850);


CREATE TABLE Printer (
	code integer PRIMARY KEY,
	model varchar(255) references Product(model),
	color varchar(1),
	"type" varchar(6),
	price integer
);

INSERT INTO Printer VALUES (0,'DL5564','y','Laser', 210);
INSERT INTO Printer VALUES (1,'DX62','n','Laser', 250);
INSERT INTO Printer VALUES (2,'2460','n','Matrix', 546);
INSERT INTO Printer VALUES (3,'XL','y','Jet', 111);


SELECT model, speed, hd
FROM PC
WHERE price < 500;

SELECT DISTINCT maker FROM Product
WHERE "type" = 'Printer';

SELECT model, ram, screen FROM Laptop
WHERE price > 1000;

SELECT * FROM Printer
WHERE color = 'y';

SELECT model, speed, hd,cd,price FROM PC
WHERE price < 600 AND (cd = '12x' OR cd = '24x');