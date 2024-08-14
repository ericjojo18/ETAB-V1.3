# -*- coding: utf-8 -*-
from datetime import datetime
from Models.Utilisateur import Utilisateur
import bcrypt
class GestionUtilisateur:
    
    #def __init__(self):
        #self.utilisateurs = {}
        
         #pour afficher le menu 
    def afficher_menu(self):
        
        while True:
            print("*" * 20)
            print("\nGESTION DES UTILISATEURS")
            print("*" * 20)
            print("\nMenu:")
            print("1: Ajouter un utilisateur")
            print("2: Supprimer un utilisateur")
            print("3: Modifier les informations du utilisateur")
            print("4: Lister les utilisateurs")
            print("5: Obtenir le dernier professeurr ajouté")
            print("6: Retour")
            print("0: Quitter")
            
            menu_choix = input("Choisissez une option: ")
            try:
                if menu_choix == '1':
                    self.ajouter_utlisateur()
                elif menu_choix == '2':
                    self.supprime_utlisateur()
                elif menu_choix == '3':
                   self.modifier_utlisateur()
                elif menu_choix == '4':
                    self.list_utlisateur() 
                elif menu_choix == '5':
                    self.dernier_utlisateur()
                elif menu_choix == '6':
                    break
                elif menu_choix =='0':
                    break
                else:
                    print("Option non valide, veuillez réessayer.")
            except ValueError as e:
                print(f"Erreur: {e}")
    
        #la fonction pour ajouter un professeur
    def ajouter_utlisateur(self):
        try:
            #id = input("Entrez votre identifiant: ")
            #if not id:
                #raise ValueError("le champ identifiant ne peut pass etre vide")
        
            pseudo = input("Entrez votre pseudo: ")
            if not pseudo:
                raise ValueError("le champ nom ne peut pass etre vide")
        
            motDePasse = input("Entrez votre mot de passe: ")
            if not motDePasse:
                raise ValueError("le champ prenom ne peut pass etre vide")
        
            mdp = bcrypt.hashpw(motDePasse.encode('utf-8'), bcrypt.gensalt())
        
            msg = Utilisateur.ajouterCompte(pseudo, mdp)
        
            #self.professeurs.append(professeur)
            #self.utilisateurs[id] = utilisateur
            print(msg)
        except ValueError as e:
            print(f"Erreur: {e}")
 
        #supprimer un professeur
    def supprime_utlisateur(self):
        #pseudo = input("\nEntrez l'identifiant unique de l'utilisateur à supprimer: ")
        pseudo = input("Entrez le pseudo de l'utilisateur à supprimer : ")
        if not Utilisateur.supprimerCompte(pseudo):
            print(f"L'utilisateur {pseudo} n'existe pas.")
        
        ## Modifier les informations du professeur

    def modifier_utlisateur(self):
        pseudo = input("\nEntrez le pseudo de l'utilisateur à modifier: ")    
             
        utilisateur = Utilisateur.recuperer_utilisateur(pseudo)
        if utilisateur:
            nouveauMotDePasse = bcrypt.hashpw(input(" Entrez le nouveau mot de passe:").encode('utf-8'),bcrypt.gensalt())
            utilisateur.modifierMotDePasse(nouveauMotDePasse)
        
     #liste des professeurs
    def list_utlisateur(self):
        Utilisateur.listerUtilisateurs()
            
        

    