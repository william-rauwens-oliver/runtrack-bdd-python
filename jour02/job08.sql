CREATE DATABASE IF NOT EXISTS zoo;

USE zoo;

CREATE TABLE IF NOT EXISTS cage (
    id INT PRIMARY KEY AUTO_INCREMENT,
    superficie REAL,
    capacite_max INTEGER
);

CREATE TABLE IF NOT EXISTS animal (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom TEXT,
    race TEXT,
    id_cage INTEGER,
    date_naissance DATE,
    pays_origine TEXT,
    FOREIGN KEY (id_cage) REFERENCES cage(id)
);

INSERT INTO cage (superficie, capacite_max) VALUES (100, 5);

INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES ('Maxime', 'Tigre', 1, '2010-01-01', 'Afrique');
INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES ('Kevin', 'Lyon', 1, '2015-05-15', 'Afrique');
INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES ('Walid', 'Ours', 1, '2018-07-10', 'Chine');


SELECT * FROM animal;

SELECT cage.id, cage.superficie, animal.id, animal.nom
FROM cage
LEFT JOIN animal ON cage.id = animal.id_cage;

SELECT SUM(superficie) AS superficie_totale FROM cage;