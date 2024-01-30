CREATE DATABASE IF NOT EXISTS metier;

USE metier;

CREATE TABLE IF NOT EXISTS employe (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT
);

INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
('Valle', 'Maxime', 3500.00, 1),
('Ngo', 'Kevin', 2800.50, 2),
('Serra', 'Mathis', 4000.75, 3),
('RauwensOliver', 'William', 3200.00, 4);


SELECT * FROM employe WHERE salaire > 3000;

CREATE TABLE IF NOT EXISTS service (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255)
);


INSERT INTO service (nom) VALUES
('DevWeb'),
('DevLogiciel'),
('CyberSecurite');

SELECT e.*, s.nom AS nom_service
FROM employe e
JOIN service s ON e.id_service = s.id;