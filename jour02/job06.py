import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="willy",
    database="LaPlateforme",
)

cursor = mydb.cursor()

cursor.execute("SELECT SUM(capacite) FROM salle")
resultat = cursor.fetchone()
capacite_totale = resultat[0]

print("La capacité de toutes les salles est de :", capacite_totale,)

cursor.close()
mydb.close()