import mysql.connector
from datetime import date

class ZooManager:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def cree_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()

    def cree_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.conn.commit()

    def lis_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def lis_animaux_cages(self):
        query = "SELECT a.*, c.superficie FROM animal a LEFT JOIN cage c ON a.id_cage = c.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def calcule_superficie_totale(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0

    def supprime_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (animal_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def connexion_ferme(self):
        self.conn.close()

zoo_manager = ZooManager("localhost", "root", "willy", "zoo")

zoo_manager.cree_cage(100, 5)
zoo_manager.cree_cage(150, 8)

zoo_manager.cree_animal("Lion", "Sauvage", 1, date(2010, 1, 1), "Afrique")
zoo_manager.cree_animal("Girafe", "Herbivore", 2, date(2015, 5, 15), "Afrique")

result_animaux = zoo_manager.lis_animaux()
print("Animaux présents dans le zoo :", result_animaux)

result_animaux_cages = zoo_manager.lis_animaux_cages()
print("Animaux présents dans les cages avec superficie respective :", result_animaux_cages)

superficie_totale = zoo_manager.calcule_superficie_totale()
print("Superficie totale de toutes les cages :", superficie_totale)

zoo_manager.supprime_animal(1)

zoo_manager.connexion_ferme()