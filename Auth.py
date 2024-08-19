# -*- coding: utf-8 -*-
from Models import Utilisateur
import bcrypt
from base.bd import DatabaseConnection 
from menu import MenuPrincipal
class Authentification:
    #def __init__(self):
        #self.pseudo = "admin"
        #self.motDePasse = "admin"
    
        
    def connexion_utilisateur(self, pseudo):
        bd = DatabaseConnection()
        connection = bd.create_connection()
        if connection: 
            cursor = connection.cursor()
            cursor.execute("SELECT pseudo, mot_de_passe FROM utilisateurs WHERE pseudo = %s", (pseudo,))
            utilisateur = cursor.fetchone()
            cursor.close()
            bd.close_connection()
            return utilisateur
        return None
    
    
    def bienvenu():
        print("*" * 20)
        print("\nBienvenue dans l'application Etab v1.3\n")
        print("*" * 20)
        print("\nCONNEXION\n")
        
    def connexion(self):    
        try:
            pseudo = input("Pseudo: ")
            if not pseudo:
                 raise ValueError("l'identifiant ne peut pass etre vide")
             
            mot_de_passe = input("mot de passe: ")
            
            if not mot_de_passe:
                 raise ValueError("le mot de passe ne peut pass etre vide")
            
            Utilisateur = self.connexion_utilisateur(pseudo)
            
            if Utilisateur and bcrypt.checkpw(mot_de_passe.encode('utf-8'), Utilisateur[1].encode('utf-8')):
                print("Connexion réussie")
                return True
            else:
                print("Connexion echoue, Veuillez réessayer")
                return False
                #utlisateur = Utlisateur(identifiant, mot_de_passe)
                #self.utilisateur.append(utlisateur)
        except ValueError as e:
            print(f"Erreur: {e}")
            return False
        

