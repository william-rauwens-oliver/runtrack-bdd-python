import mysql.connector

class SalarieManager:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def cree_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()

    def lis_employe(self, salary):
        query = "SELECT * FROM employe WHERE salaire > %s"
        values = (salary,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    def lis_service_et_employe(self):
        query = "SELECT e.*, s.nom AS nom_service FROM employe e JOIN service s ON e.id_service = s.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def met_a_jour_employe(self, employe_id, nom, prenom, salaire, id_service):
        query = "UPDATE employe SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        values = (nom, prenom, salaire, id_service, employe_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprime_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def obtenir_employe_par_id(self, employe_id):
        query = "SELECT * FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result

    def connexion_ferme(self):
        self.conn.close()

salarie_manager = SalarieManager("localhost", "root", "willy", "metier")

salarie_manager.cree_employe("Paul", "Franc", 3500.50, 2)

salarie_manager.met_a_jour_employe(1, "Bert", "François", 4000.0, 3)

result_above_3000 = salarie_manager.lis_employe(3000)
print("Employés avec salaire > 3000 :", result_above_3000)

result_with_service = salarie_manager.lis_service_et_employe()
print("Employés avec leur service respectif :", result_with_service)

salarie_manager.supprime_employe(8)

salarie_manager.connexion_ferme()