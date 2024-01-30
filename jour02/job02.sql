import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "willy",
database = "LaPlateforme",
)

cursor = mydb.cursor()

CREATE TABLE etage (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    numero INT,
    superficie INT
);

CREATE TABLE salle (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT,
    FOREIGN KEY (id_etage) REFERENCES etage(id)
);