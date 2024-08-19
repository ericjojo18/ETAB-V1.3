from Models.ICRUDEleve import ICRUDEleve
from base.bd import DatabaseConnection
from mysql.connector import Error
import datetime

class Eleve(ICRUDEleve):
    """
    Eleve est une classe qui hérite des méthodes de ICRUDEleve
    """
    
    __eleves = []

    def __init__(self, id, nom, prenom, ville, date_naissance, telephone, classe, matricule):
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__ville = ville 
        self.__date_naissance = date_naissance 
        self.__telephone = telephone
        self.__classe = classe
        self.__matricule = matricule 

    def __str__(self):
        return (f"Id: {self.get_id()}, Nom: {self.get_nom()}, Prénom: {self.get_prenom()}, "
                f"Ville: {self.get_ville()}, Date de naissance: {self.get_date_naissance()}, "
                f"Téléphone: {self.get_telephone()}, Classe: {self.get_classe()}, Matricule: {self.get_matricule()}")

    # Accesseurs
    def get_id(self):
        return self.__id

    def get_date_naissance(self):
        return self.__date_naissance 

    def get_ville(self):
        return self.__ville

    def get_prenom(self):
        return self.__prenom

    def get_nom(self):
        return self.__nom   

    def get_classe(self):
        return self.__classe 
    
    def get_matricule(self):
        return self.__matricule

    def get_telephone(self):
        return self.__telephone    

    # Mutateurs
    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_nom(self, nom):
        self.__nom = nom

    def set_ville(self, ville):
        self.__ville = ville

    def set_date_naissance(self, date_naissance):
        self.__date_naissance = date_naissance 

    def set_telephone(self, telephone):
        self.__telephone = telephone

    def set_classe(self, classe):
        self.__classe = classe            

    def set_matricule(self, matricule):
        self.__matricule = matricule
        
    def obtenir_age(self):
        date_present = datetime.date.today()
        date_naissance = datetime.datetime.strptime(self.__date_naissance, "%d/%m/%Y")
        age = date_present.year - date_naissance.year - ((date_present.month, date_present.day) < (date_naissance.month, date_naissance.day))
        return age

    # Implémentation des méthodes CRUD
    @classmethod
    def ajouter(cls, eleve):
        bd = DatabaseConnection()
        conn = bd.create_connection()
        try:
            if conn.is_connected():
                curseur = conn.cursor()
                curseur.execute(
                    "INSERT INTO eleves (nom, prenom, ville, date_naissance, telephone, classe, matricule) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (eleve.get_nom(), eleve.get_prenom(), eleve.get_ville(), str(eleve.get_date_naissance()), eleve.get_telephone(), eleve.get_classe(), eleve.get_matricule())
                )
                conn.commit()
                print(f"L'élève {eleve.get_prenom()} {eleve.get_nom()} a bien été ajouté dans la base de données.")
        except Exception as e:
            print(f"Erreur lors de l'ajout : {e}")
        finally:
            if conn.is_connected():
                curseur.close()
                conn.close()

    @classmethod
    def modifier(cls, eleve):
        bd = DatabaseConnection()
        conn = bd.create_connection()
        try:
            if conn.is_connected():
                curseur = conn.cursor()
                curseur.execute(
                    "UPDATE eleves SET nom = %s, prenom = %s, ville = %s, date_naissance = %s, telephone = %s, classe = %s, matricule = %s WHERE id = %s",
                    (eleve.get_nom(), eleve.get_prenom(), eleve.get_ville(), eleve.get_date_naissance(), eleve.get_telephone(), eleve.get_classe(), eleve.get_matricule(), eleve.get_id())
                )
                conn.commit()
                print(f"L'élève avec l'ID {eleve.get_id()} a été modifié avec succès.")
                return True
        except Exception as e:
            print(f"Erreur lors de la modification : {e}")
        finally:
            if conn.is_connected():
                curseur.close()
                conn.close()
        return False

    @classmethod
    def supprimer(cls, id):
        bd = DatabaseConnection()
        conn = bd.create_connection()
        if conn.is_connected():
            curseur = conn.cursor()
            curseur.execute("DELETE FROM eleves WHERE id = %s", (id,))
            conn.commit()
            print(f"L'élève avec ID {id} a bien été supprimé de la base de données.")
            conn.close()

    @classmethod
    def obtenirEleve(cls):
        bd = DatabaseConnection()
        conn = bd.create_connection()
        try:
            if conn.is_connected():
                curseur = conn.cursor()
                curseur.execute("SELECT id, nom, prenom, date_naissance, ville, telephone, classe, matricule FROM eleves")
                eleves = curseur.fetchall()
                if eleves:
                    return [Eleve(*eleve) for eleve in eleves]
                else:
                    print("Aucun élève trouvé.")
                    return []
        except Error as e:
            print(f"Erreur : {e}")
        finally:
            if conn.is_connected():
                curseur.close()
                conn.close()
        return []

    @classmethod
    def Obtenir(cls, id):
        """
        Récupère un élève de la base de données en fonction de son identifiant.
    
        Args:
            id (int): L'identifiant de l'élève.
    
        Returns:
            Eleve: L'objet Eleve correspondant à l'identifiant, ou None si aucun élève n'est trouvé.
        """
        bd = DatabaseConnection()
        conn = bd.create_connection()
        try:
            conn = bd.create_connection()
            curseur = conn.cursor()
            curseur.execute("SELECT id, nom, prenom, ville, date_naissance, telephone, classe, matricule FROM eleves WHERE id = %s", (id,))
            eleve_db = curseur.fetchone()
            if eleve_db:
                return Eleve(*eleve_db)
            else:
                print("Aucun élève trouvé avec cet identifiant.")
        except Error as e:
            print(f"Erreur : {e}")
        return None

    def afficher_info(self):
        print(f"Classe: {self.get_classe()}")
