from Models.ICRUDProfesseur import ICRUDProfesseur
from Models.IEducation import IEducation
from base.bd import DatabaseConnection
from mysql.connector import Error
import datetime

class Professeur(ICRUDProfesseur, IEducation): 
    def __init__(self,id, nom, prenom, ville, date_naissance, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion):
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__ville = ville
        self.__date_naissance = date_naissance
        self.__telephone = telephone
        self.__vacant = vacant
        self.__matiere_enseigne = matiere_enseigne
        self.__prochain_cours = prochain_cours
        self.__sujet_prochaine_reunion = sujet_prochaine_reunion
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

    def get_vacant(self):
        return self.__vacant 
    
    def get_matiere_enseignee(self):
        return self.__matiere_enseigne

    def get_telephone(self):
        return self.__telephone  
    
    def get_prochain_cours(self):
        return self.__prochain_cours
    
    def get_sujet_prochaine_reunion(self):
        return self.__sujet_prochaine_reunion

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

    def set_vacant(self, vacant):
        self.__vacant = vacant           

    def set_matiere_enseignee(self, matiere_enseigne):
        self.__matiere_enseigne = matiere_enseigne
        
    def set_prochain_cours(self, prochain_cours):
        self.__prochain_cours = prochain_cours

    def set_sujet_prochaine_reunion(self, sujet_prochaine_reunion):
        self.__sujet_prochaine_reunion = sujet_prochaine_reunion
        
    def __str__(self):
        return (f"Id: {self.get_id()}, "
                f"Nom: {self.nom}, "
                f"Prénom: {self.prenom}, "
                f"Ville: {self.ville}, "
                f"Date de naissance: {self.date_naissance.strftime('%d/%m/%Y')}, "
                f"Téléphone: {self.telephone}, "
                f"Vacant: {'Oui' if self.vacant else 'Non'}, "
                f"Matière: {self.matiere_enseigne}, "
                f"Cours: {self.prochain_cours}, "
                f"Sujet Réunion: {self.sujet_prochaine_reunion}")

    
    @staticmethod
    def ajouter(professeur):
        """Ajoute un nouvel professeur à la base de données."""
        bd = DatabaseConnection()
        connection = bd.create_connection()
        try:
            if connection.is_connected():
                curseur = connection.cursor()
                curseur.execute(
                    "INSERT INTO professeurs (nom, prenom, ville, date_naissance, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (professeur.get_nom(), professeur.get_prenom(), professeur.get_ville(), str(professeur.get_date_naissance()), professeur.get_telephone(), professeur.get_vacant(), professeur.get_matiere_enseignee(), professeur.get_prochain_cours(), professeur.get_sujet_prochaine_reunion())
                )
                connection.commit()
                print(f"Le professeur {professeur.get_prenom()} {professeur.get_nom()} a bien été ajouté dans la base de données.")
        except Exception as e:
            print(f"Erreur lors de la création du compte: {e}")
        finally:
            if connection.is_connected():
                curseur.close()
                connection.close()

    @classmethod
    def modifier(cls, professeur):
        bd = DatabaseConnection()
        conn = bd.create_connection()
        try:
            if conn.is_connected():
                curseur = conn.cursor()
                curseur.execute(
                    "UPDATE professeurs SET nom = %s, prenom = %s, ville = %s, date_naissance = %s, telephone = %s, vacant = %s, matiere_enseigne = %s, prochain_cours = %s, sujet_prochaine_reunion = %s WHERE id = %s",
                    (professeur.get_nom(), professeur.get_prenom(), professeur.get_ville(), professeur.get_date_naissance(), professeur.get_telephone(), professeur.get_vacant(), professeur.get_matiere_enseignee(), professeur.get_prochain_cours(), professeur.get_sujet_prochaine_reunion(), professeur.get_id())
                )
                conn.commit()
                print(f"Le professeur avec l'ID {professeur.get_id()} a été modifié avec succès.")
                return True
        except Exception as e:
            print(f"Erreur lors de la modification : {e}")
        finally:
            if conn.is_connected():
                curseur.close()
                
        return False

    @staticmethod
    def supprimer( id):
        bd = DatabaseConnection()
        conn = bd.create_connection()
        try:
            if conn.is_connected():
                curseur = conn.cursor()
                curseur.execute("DELETE FROM professeurs WHERE id = %s", (id,))
                conn.commit()
                print(f"Le professeur avec ID {id} a bien été supprimé de la base de données.")
        except Error as e:
            print(f"Erreur lors de la suppression : {e}")
        finally:
            if conn.is_connected():
                curseur.close()
                

    @classmethod
    def obtenirProf(cls):
        bd = DatabaseConnection()
        conn = bd.create_connection()
        try:
            if conn.is_connected():
                curseur = conn.cursor()
                curseur.execute("SELECT id, nom, prenom, date_naissance, ville, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion FROM professeurs")
                professeurs = curseur.fetchall()
                if professeurs:
                    return [Professeur(*professeur) for professeur in professeurs]
                else:
                    print("Aucun professeur trouvé.")
                    return []
        except Error as e:
            print(f"Erreur : {e}")
        finally:
            if conn.is_connected():
                curseur.close()
                
        return []

    @classmethod
    def Obtenir(cls, id):
        bd = DatabaseConnection()
        conn = bd.create_connection()
        try:
            if conn.is_connected():
                curseur = conn.cursor()
                curseur.execute("SELECT * FROM professeurs WHERE id = %s", (id,))
                professeur_db = curseur.fetchone()
                if professeur_db:
                    return Professeur(*professeur_db)
                else:
                    print("Aucun professeur trouvé avec cet identifiant.")
        except Error as e:
            print(f"Erreur : {e}")
        finally:
            if conn.is_connected():
                curseur.close()

        return None

    def afficher_info(self):
        print(f"Nom: {self.get_nom()}, Prénom: {self.get_prenom()}, Ville: {self.get_ville()}, "
              f"Date de naissance: {self.get_date_naissance()}, Téléphone: {self.get_telephone()}, "
              f"Matière: {self.get_matiere_enseignee()}, Prochain cours: {self.get_prochain_cours()}, "
              f"Sujet prochaine réunion: {self.get_sujet_prochaine_reunion()}")

    def enseigner(self):
        print(f"Enseigne la matière: {self.get_matiere_enseignee()}")
       
    def preparer_cours(self):
        print(f"Préparer le prochain cours: {self.get_prochain_cours()}")
        
    def assister_reunion(self):
        print(f"Doit assister à une réunion: {self.get_sujet_prochaine_reunion()}")
