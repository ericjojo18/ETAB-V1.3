# -*- coding: utf-8 -*-
from datetime import datetime
from base.bd import DatabaseConnection
from base import req_utilisateur
class Utilisateur:
    
    __idunique = 0
    __utilisateurs = []
    def __init__(self, pseudo, motDePasse, dateCreation):
        Utilisateur.__idunique += 1
        self.__id = Utilisateur.__idunique
        self.__pseudo = pseudo
        self.__motDePasse = motDePasse
        self.__dateCreation = dateCreation
        Utilisateur.__utilisateurs.append(self)
        
         # Retourne une représentation sous forme de chaîne de l'utilisateur. 
    def __str__(self):
        return f"Utilisateur n0 {self.__id} : {self.__pseudo} crée le {self.__dateCreation}"
    
    # Retourne l'identifiant unique de l'utilisateur
    @property
    def id(self):
        return self.__id

    # Retourne le pseudo de l'utilisateur
    @property
    def pseudo(self):
        return self.__pseudo  
    
    # Retourne la date de création du compte de l'utilisateur
    @property
    def dateCreation(self):
        return self.__dateCreation

    def nouveauMotDePasse(self, nouveauMotDePasse):
        self.__motDePasse = nouveauMotDePasse
        
    def authentification(self, identifiant, motDePasse):
        if self.__pseudo == identifiant and self.__motDePasse == motDePasse :
            return True
        return False
    
    @classmethod
    def ajouterCompte(cls, pseudo, motDePasse):
        """Ajoute un nouvel utilisateur à la base de données."""
        bd = DatabaseConnection()
        dateCreation = datetime.now()
        nouvel_utilisateur = cls(pseudo, motDePasse, dateCreation)
        
        connection = bd.create_connection()
        if connection and connection.is_connected():
            try:
                curseur = connection.cursor()
                req_utilisateur.ajouter_utilisateur(curseur, pseudo, motDePasse)  # Fonction pour insérer dans la BD
                connection.commit()
                nouvel_utilisateur.__id = curseur.lastrowid  # Récupérer l'ID de l'utilisateur créé
                return f"Compte créé avec succès !!\n-->Pseudo : {pseudo}"
            except Exception as e:
                print(f"Erreur lors de la création du compte: {e}")
            finally:
                curseur.close()
                connection.close()
        return f"Échec de la connexion à la base de données."

    def modifierMotDePasse(self, nouveauMotDePasse):
        """Modifie le mot de passe de l'utilisateur dans la base de données."""
        
        bd = DatabaseConnection()
        self.__motDePasse = nouveauMotDePasse
        connection = bd.create_connection()
        if connection and connection.is_connected():
            try:
                curseur = connection.cursor()
                req_utilisateur.modifier_mot_de_passe(curseur, self.__pseudo, nouveauMotDePasse)
                connection.commit()
                print(f"Mot de passe modifié pour l'utilisateur {self.__pseudo}")
            except Exception as e:
                print(f"Erreur lors de la modification du mot de passe: {e}")
            finally:
                curseur.close()
                bd.close_connection()

    @classmethod
    def supprimerCompte(cls, pseudo):
        """Supprime un utilisateur de la base de données."""
        bd = DatabaseConnection()
        connection = bd.create_connection()
        if connection and connection.is_connected():
            try:
                curseur = connection.cursor()
                req_utilisateur.supprimer_utilisateur(curseur, pseudo)  # Fonction pour supprimer de la BD
                connection.commit()
                print(f"Utilisateur {pseudo} supprimé.")
            except Exception as e:
                print(f"Erreur lors de la suppression de l'utilisateur: {e}")
            finally:
                curseur.close()
                bd.close_connection()

    @classmethod
    def listerUtilisateurs(cls):
        """Liste tous les utilisateurs de la base de données."""
        bd = DatabaseConnection()
        connection = bd.create_connection()
        utilisateurs = []
        if connection and connection.is_connected():
            try:
                curseur = connection.cursor()
                utilisateurs_db = req_utilisateur.lister_utilisateurs(curseur)  # Fonction pour lister les utilisateurs
                for user in utilisateurs_db:
                    print(f"ID: {user[0]}, Pseudo: {user[1]}, Date de création: {user[2]}")
                return utilisateurs
            except Exception as e:
                print(f"Erreur lors de la récupération des utilisateurs: {e}")
            finally:
                curseur.close()
                bd.close_connection()
        return utilisateurs

    @classmethod
    def recuperer_utilisateur(cls, pseudo):
        bd = DatabaseConnection()
        connection = bd.create_connection()
        if connection and connection.is_connected():
            try:
                curseur = connection.cursor()
                result = req_utilisateur.recuperer_utilisateur(curseur, pseudo)
                if result:
                    return cls(result[0], result[1], result[2]) 
            except Exception as e:
                print(f"Erreur lors de la création du compte: {e}")
            finally:
                curseur.close()
                bd.close_connection()
        return None
    
    