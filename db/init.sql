CREATE DATABASE clsStudents;
use clsStudents;

CREATE TABLE IF NOT EXISTS cls_students (
    `id` INT AUTO_INCREMENT,
    `Name` VARCHAR(19) CHARACTER SET utf8,
    `Room` VARCHAR(6) CHARACTER SET utf8,
    `Class` VARCHAR(5) CHARACTER SET utf8,
    `Age` NUMERIC(4, 2),
    PRIMARY KEY (`id`)
);

/* CREATE TABLE */
CREATE TABLE IF NOT EXISTS tblUsers(
  id int AUTO_INCREMENT,
  userName VARCHAR(100),
  userEmail VARCHAR(100),
  userPassword VARCHAR(100),
  userHash VARCHAR(100),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS tblErrors(
  errCode int AUTO_INCREMENT,
  errName VARCHAR(100),
  errMessage VARCHAR(100),
  errNextPage VARCHAR(100),
  PRIMARY KEY (errCode)
);

CREATE TABLE IF NOT EXISTS  labels (
  `id` INT AUTO_INCREMENT,
  `label` VARCHAR (255) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS  val (
  `id` INT AUTO_INCREMENT,
  `values` INT NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS  colors (
  `id` INT AUTO_INCREMENT,
  `colors` VARCHAR (255) NOT NULL,
  PRIMARY KEY (`id`)
);

insert into `labels`(`id`,`label`) values
(1,'JAN'),
(2,'FEB'),
(3,'MAR'),
(4,'APR'),
(5,'MAY'),
(6,'JUN'),
(7,'JUL'),
(8,'AUG'),
(9,'SEP'),
(10,'OCT'),
(11,'NOV'),
(12,'DEC');

insert into `val`(`id`,`values`) values
(1, 967.67),
(2,1190.89),
(3,1079.75),
(4,1349.19),
(5,2328.91),
(6,2504.28),
(7,2873.83),
(8,4764.87),
(9,4349.29),
(10,6458.30),
(11,9907),
(12,16297);

insert into `colors`(`id`,`colors`) values
    (1,'#F7464A'), (2,'#46BFBD'), (3,'#FDB45C'), (4,'#FEDCBA'),
    (5,'#ABCDEF'), (6,'#DDDDDD'), (7,'#ABCABC'), (8,'#4169E1'),
    (9,'#C71585'), (10,'#FF4500'),(11,'#FEDCBA'),(12,'#46BFBD');

INSERT INTO tblUsers(userName, userEmail, userPassword, userHash) VALUES
    ('username1', 'username1@gmail.com', 'password1',''),
    ('username2', 'username2@gmail.com', 'password2',''),
    ('username3', 'username3@gmail.com', 'password3',''),
    ('username4', 'username4@gmail.com', 'password4',''),
    ('username5', 'username5@gmail.com', 'password5','');

INSERT INTO tblErrors(errCode, errName, errMessage, errNextPage) VALUES
    ('404', 'USER_NOT_FOUND','User name not found', 'signup'),
    ('405', 'USER_EXISTS','User name already exists.', 'login'),
    ('406', 'EMAIL_NOT_VERIFIED','Please verify your email before trying to login.', 'login'),
    ('407', 'INVALID_LOGIN','Please check your email id/password and try again.', 'login'),
    ('200', 'USER_CREATED','User created successfully. Please check your email for login instructions.', 'login'),
    ('201', 'EMAIL_VERIFIED','Email verified successfully. Please proceed to login.', 'login');

INSERT INTO cls_students (Name, Room, Class, Age) VALUES
    ('Jane Doe',' "RPS"',' "Chem"',14),
    ('Smith Rock',' "RPS"',' "Chem"',15),
    ('Ramoe Max',' "RPS"',' "Chem"',15),
    ('Kevin Olive',' "RPS"',' "Chem"',15),
    ('Davis Taylor',' "RPS"',' "Chem"',15),
    ('White Trustman',' "RPS"',' "Chem"',15),
    ('Mike Pat',' "RPS"',' "Chem"',15),
    ('Kajal Patel',' "RPS"',' "Chem"',15),
    ('Shreya Patel',' "RPS"',' "Chem"',15),
    ('Adam Johnson',' "RPS"',' "Chem"',15),
    ('Ryan Matt',' "RPS"',' "Chem"',15),
    ('Fred Thomas',' "RPS"',' "Chem"',15),
    ('Nic Harris',' "RPS"',' "Chem"',14),
    ('Brian White',' "RPS"',' "Chem"',14),
    ('Core Martin',' "RPS"',' "Chem"',14),
    ('Max Harris',' "RPS"',' "Chem"',14),
    ('Max Gibbons',' "RPS"',' "Chem"',14),
    ('Erik Bedard',' "RPS"',' "Chem"',14),
    ('Wilson Penn',' "RPS"',' "Chem"',14),
    ('Adam Loewen',' "RPS"',' "Chem"',14),
    ('Daniel Cabrera',' "RPS"',' "Bio"',14),
    ('Steve Thomas',' "RPS"',' "Bio"',14),
    ('Jaret Wright',' "RPS"',' "Bio"',14),
    ('Grace Benson',' "RPS"',' "Bio"',14),
    ('Scott Williamson',' "RPS"',' "Bio"',14),
    ('John Doe',' "RPS"',' "Bio"',14),
    ('Danys Baez',' "RPS"',' "Bio"',14),
    ('Chad Find',' "RPS"',' "Bio"',14),
    ('Jam Walker',' "RPS"',' "Bio"',14),
    ('Brian Fun',' "RPS"',' "Bio"',14,
    ('Kurt Birkins',' "RPS"',' "Bio"',14),
    ('James April',' "RPS"',' "Bio"',14),
    ('Sendy Rleal',' "RPS"',' "Bio"',14),
    ('Chris Mal',' "RPS"',' "Bio"',14),
    ('Jeremy Guthrie',' "RPS"',' "Bio"',14),
    ('A.J. Pierzynski',' "GYM"',' "Bio"',14),
    ('Toby Ray',' "GYM"',' "Bio"',14),
    ('Paul Konerko',' "GYM"',' "Bio"',14),
    ('Tadahito Hall',' "GYM"',' "Bio"',14),
    ('Juan Uribe',' "GYM"',' "Bio"',14),
    ('Alex Iquichi',' "GYM"',' "Bio"',14),
    ('Jo Crede',' "GYM"',' "Bio"',14),
    ('Josh Jones',' "GYM"',' "Bio"',14),
    ('Ryan Sweeney',' "GYM"',' "Bio"',14),
    ('Brian N. Fields',' "GYM"',' "Bio"',14),
    ('Lui Terrero',' "GYM"',' "Phy"',16),
    ('Pablo Anderson',' "GYM"',' "Phy"',16),
    ('Scott Podsednik',' "GYM"',' "Phy"',16),
    ('Jermaine Dye',' "GYM"',' "Phy"',16),
    ('Darin Erstad',' "GYM"',' "Phy"',16),
    ('Rob Mackowiak',' "GYM"',' "Phy"',16),
    ('Jim Thome',' "GYM"',' "Phy"',16),
    ('Jerrie Owens',' "GYM"',' "Phy"',15),
    ('Charlie Haeger',' "GYM"',' "Phy"',16),
    ('Heathy Phillips',' "GYM"',' "Phy"',16),
    ('Gavin Floyd',' "GYM"',' "Phy"',17),
    ('Josel Contreras',' "GYM"',' "Phy"',17),
    ('Jon Garland',' "GYM"',' "Phy"',17),
    ('Javier Vazquez',' "GYM"',' "Phy"',17),
    ('Mark Buehrle',' "GYM"',' "Phy"',17),
    ('Mike MacDougal',' "GYM"',' "Phy"',17),
    ('David Aardsma',' "GYM"',' "Phy"',17),
    ('Andre Sisco',' "GYM"',' "Phy"',17),
    ('Matt Thornton',' "GYM"',' "Phy"',17),
    ('Bob Jenks',' "GYM"',' "Phy"',17),
    ('Boone Logan',' "GYM"',' "Phy"',17),
    ('SeDWN Tracey',' "GYM"',' "Phy"',17),
    ('Nicky Masset',' "GYM"',' "Phy"',17),
    ('Jose Molina',' "DWN"',' "Phy"',17),
    ('Jeffrey Math',' "DWN"',' "Phy"',17),
    ('Mike Napoli',' "DWN"',' "Phy"',17),
    ('Caisey Kotchman',' "DWN"',' "Phy"',17),
    ('Kendrick Morales',' "DWN"',' "Phy"',17),
    ('Shea Hillenbrand',' "DWN"',' "Phy"',17),
    ('Robb Quinlan',' "DWN"',' "Phy"',17),
    ('Howie Kendrick',' "DWN"',' "Phy"',17),
    ('Orlando Cabrera',' "DWN"',' "Phy"',17),
    ('Erick Aybar',' "DWN"',' "Phy"',17),
    ('Dallas McPherson',' "DWN"',' "Phy"',17),
    ('Maicer Izturis',' "DWN"',' "Phy"',17),
    ('Reggina Willits',' "DWN"',' "Phy"',17),
    ('Tommy Murphy',' "DWN"',' "Phy"',17),
    ('Terry Evans',' "DWN"',' "Phy"',16),
    ('Gary Matthews Jr.',' "DWN"',' "Phy"',16),
    ('Garret Anderson',' "DWN"',' "Phy"',16),
    ('Vladimir Guerr',' "DWN"',' "Phy"',16),
    ('Chone Figgins',' "DWN"',' "Phy"',18),
    ('Juan River',' "DWN"',' "Phy"',18),
    ('John Lakey',' "DWN"',' "Phy"',18),
    ('Bartolo Colon',' "DWN"',' "Phy"',18),
    ('Kelvim Escobar',' "DWN"',' "Phy"',18),
    ('Dustin Moeley',' "DWN"',' "Phy"',18),
    ('Ervin SantDWN',' "DWN"',' "Phy"',18),
    ('Joe Sauders',' "DWN"',' "Phy"',16),
    ('Jered Weaver',' "DWN"',' "Phy"',16),
    ('Chris Resop',' "DWN"',' "Phy"',16),
    ('Phillip Seibel',' "DWN"',' "Phy"',16),
    ('Justine Baker',' "DWN"',' "Phy"',16),
    ('Dan Oliver',' "DWN"',' "Phy"',16),
    ('Hector Ramirez',' "DWN"',' "Phy"',17),
    ('Scotty Hanson',' "DWN"',' "Phy"',16),
    ('Andrew Green',' "DWN"',' "Phy"',17),
    ('Krupa Racey',' "DWN"',' "Phy"',16),
    ('Nikita Stone',' "UPS"',' "Phy"',16),
    ('Lexie Williamson',' "UPS"',' "Phy"',16),
    ('Georgia Williams',' "UPS"',' "Phy"',16),
    ('Keya Finds',' "UPS"',' "Phy"',16),
    ('Dan Range',' "UPS"',' "Phy"',16),
    ('Adam Hill',' "UPS"',' "Phy"',16);