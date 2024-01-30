import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="willy",
    database="LaPlateforme",
)

cursor = mydb.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")
resultat = cursor.fetchone()
superficie_totale = resultat[0]

print("La superficie de La Plateforme est de", superficie_totale, "m2")

cursor.close()
mydb.close()