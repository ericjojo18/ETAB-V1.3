#la classe Eleve qui herite des methodes et des propriétés de la classe personne en utilisant la fonction super()        
from Models.Personne import Personne
from Models.ICRUDEleve import ICRUDEleve
from base.bd import create_connection
from mysql.connector import Error
class Eleve(Personne, ICRUDEleve):
    """
    Eleve est une classe qui herite de Personne et de ICRUDEleve
    """
    
    __eleves = []
    #initialisation des propriétés d'un eleve
    def __init__(self, id,nom, prenom, ville, dateNaissance, telephone, classe, matricule):
        super().__init__( id, nom, prenom, ville, dateNaissance, telephone)
        self.__classe =  classe
        self.__matricule = matricule 
        
    #Retourne sous forme de chaine de l'élève
    @property 
    def get_matricule(self):
        return self.__matricule
    
    @property 
    def get_classe(self):
        return self.__classe

    def set_classe(self, classe):
        self.__classe = classe            

    def set_matricule(self, matricule):
        self.__matricule = matricule

    # Implémentation des méthodes CRUD
    # Ajouter un élève
    def ajouter(eleve):
        #inserer personne
        conn = create_connection()
        if conn.is_connected():
            curseur = conn.cursor()
            curseur.execute("INSERT INTO personnes (nom, prenom, date_naissance, ville, telephone) VALUES (%s, %s, %s, %s, %s)", 
                            (eleve.get_nom, eleve.get_prenom, eleve.get_date_naissance, eleve.get_ville, eleve.get_telephone))
            conn.commit()
            id_personne = curseur.lastrowid
            
            curseur.execute("INSERT INTO eleves (id_personne, classe, matricule ) VALUES (%s, %s, %s)",
                            (id_personne, eleve.get_classe, eleve.get_matricule))
            conn.commit()
            print(f"l'éléve {eleve.get_prenom} {eleve.get_nom} a bien été ajoutée dans la base de données.")
            conn.close()
        #Eleve.__eleves.append(eleve)

    # modifier un élève
    def modifier(eleve):
        conn = create_connection()
        if conn.is_connected():
            curseur = conn.cursor()
            
            try:
                # Vérifier si l'élève existe dans la base de données
                curseur.execute("SELECT id_personne FROM eleves WHERE id_personne = %s", (eleve.get_id(),))
                if curseur.fetchone() is None:
                    print(f"Aucun élève trouvé avec l'ID {eleve.get_id()}.")
                    conn.close()
                    return False

                # Mettre à jour les informations de l'élève dans la base de données
                curseur.execute(
                    "UPDATE personnes SET nom = %s, prenom = %s, date_naissance = %s, ville = %s, telephone = %s WHERE id = %s",
                    (eleve.get_nom(), eleve.get_prenom(), eleve.get_date_naissance(), eleve.get_ville(), eleve.get_telephone(), eleve.get_id())
                )
                curseur.execute(
                    "UPDATE eleves SET classe = %s, matricule = %s WHERE id_personne = %s",
                    (eleve.get_classe(), eleve.get_matricule(), eleve.get_id())
                )
                conn.commit()

                # Mettre à jour l'élève en mémoire
                for index, eleve_existe in enumerate(Eleve.__eleves):
                    if eleve_existe.get_id() == eleve.get_id():
                        Eleve.__eleves[index] = eleve
                        print(f"L'élève avec l'ID {eleve.get_id()} a été modifié avec succès.")
                        break
                else:
                    print(f"L'élève avec l'ID {eleve.get_id()} n'a pas été trouvé dans la liste.")
                    conn.close()
                    return False
                
            except Exception as e:
                print(f"Erreur lors de la modification : {e}")
                return False
            
            finally:
                conn.close()
            
        return True


    # supprimer un élève 
    def supprimer(id):
        conn = create_connection()
        if conn.is_connected():
            curseur = conn.cursor()

            # Supprimer d'abord l'élève de la table `eleves`
            curseur.execute("DELETE FROM eleves WHERE id_personne = %s", (id,))
            conn.commit()

            # Ensuite, supprimer la personne de la table `personnes`
            curseur.execute("DELETE FROM personnes WHERE id = %s", (id,))
            conn.commit()

            print(f"L'élève avec ID {id} a bien été supprimé de la base de données.")
            conn.close()


    # Obtenir les élèves
    def obtenirEleve():
        try:
            conn = create_connection()
            if conn.is_connected():
                curseur = conn.cursor()
                curseur.execute(" SELECT personnes.id, personnes.nom, personnes.prenom, personnes.ville, personnes.date_naissance, personnes.telephone, eleves.classe, eleves.matricule FROM personnes JOIN eleves ON personnes.id = eleves.id_personne")
                eleves = curseur.fetchall()
            
                if not eleves:
                    return None
       
            return eleves
        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if conn.is_connected():
                curseur.close()
                conn.close()
            
                 


    # Obtenir un élève par son id
    def Obtenir(id):
        try:
            conn = create_connection()
            if conn.is_connected():
                curseur = conn.cursor()
                curseur.execute("SELECT * FROM personnes WHERE id = %s",(id,))
                eleves = curseur.fetchone()
            
                if  eleves:
                    return None
       
            return eleves
        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if conn.is_connected():
                curseur.close()
                conn.close()
        

#afficher les informations de l'élève et la classe      
    def afficher_info(self):
         super().afficher_info()
         print(f"classe:{self.classe}")
