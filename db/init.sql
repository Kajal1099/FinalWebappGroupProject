CREATE DATABASE charts;
use charts;


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
)


ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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

