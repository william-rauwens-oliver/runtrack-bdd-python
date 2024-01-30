import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "willy",
database = "LaPlateforme",
)

cursor = mydb.cursor()

cursor.execute(

"INSERT INTO etage (nom, numero, surface) VALUES ('RDC', 0, 500), ('R+1', 1, 500)");

cursor.execute(

"INSERT INTO salle (nom, id_etage, capacite) VALUES ('Lounge', 1, 100), ('Studio Son', 1, 5), ('Broadcasting', 2, 50), ('Bocal Peda', 2, 4), ('Coworking', 2, 80), ('Studio Video', 2, 5)");

mydb.commit()
cursor.close()
mydb.close()