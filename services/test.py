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
        
        #try:
            #if not id:
                #raise ValueError("l'identifiant ne peut pas etre vide.")
            #if id in self.utilisateurs:
               # del self.utilisateurs[id]
                #self.professeurs.remove(id)
                #print("utilisateur supprimé avec succès.")
            #else:
              #  print("Aucun utilisateur trouvé avec cet identifiant.")
        #except ValueError as e:
         #   print(f"Erreur: {e}")  
        
        ## Modifier les informations du professeur

    def modifier_utlisateur(self):
        pseudo = input("\nEntrez le pseudo de l'utilisateur à modifier: ")         
        
        try:
            utilisateur = Utilisateur.trouverCompte(pseudo)
            #verifier si l'id existe
            if not utilisateur:
                print("Aucun utilisateur trouvé avec ce pseudo.")
                return
                #return
        
            utilisateur = self.utilisateurs[id]
        
            while True:
                print("\n1: Modifier le nom")
                print("2: Modifier le pseudo")
                print("3: Modifier le mot de passe")
                print("7: Retour")
                print("8: Accueil")
            
                menu_modify = input("Choisissez une option: ")    
            
                #modifier le nom
                if menu_modify == '1':
                    new_pseudo = input("Entrez le nouveau pseudo: ") 
                    if not new_pseudo:
                        raise ValueError("l'identifiant ne peut pas etre vide.")      
                    utilisateur.pseudo = new_pseudo
            
                #modifier le prénom
                elif menu_modify == '2':
                    new_motDePasse = input("Entrez le mot passe: ") 
                    if not new_motDePasse:
                        raise ValueError("le mot passe ne peut pas etre vide.")        
                    new_motDePasse.new_motDePasse = new_motDePasse
                
                #modifier l'identifiant    
                elif menu_modify == '6':
                    new_id = input("Entrez le nouvel identifiant: ")  
                    if not new_id:
                        raise ValueError("l'identifiant ne peut pas etre vide.")       
                    self.utilisateur[new_id] = self.utilisateur.pop(id)
                    id = new_id
                elif menu_modify == '7':
                    break
                elif menu_modify == '8':
                    
                    break
                else:
                    print("Option invalide. Veuillez réessayer.")
        except ValueError as e:
            print(f"Erreur: {e}")
        
     #liste des professeurs
    def list_utlisateur(self):
        if not self.utilisateurs:
            print("Aucun professeur trouvé.")
            return
        print("\nListe des utilisateurs :")
        for utilisateur in self.utilisateurs.values():
            print("\nID:", utilisateur.id)
            print("Pseudo:", utilisateur.pseudo)
            print("Mot de passe: ", utilisateur.motDePasse)
            print("-" * 20) 
            
        #Obtenir le dernier professeur ajouté

    def dernier_utlisateur(self):
        #if self.professeurs:
        # print(self.professeurs[-1])
        #else:
            #print("Aucun professeur trouvé.")
            
            if self.utilisateurs:
                dernier = next(reversed(self.utilisateurs.values()))
                print("\nDernier élève ajouté :")
                print("\nID:", dernier.id)
                print("Pseudo:", dernier.pseudo)
                print("Mot de passe: ", dernier.motDePasse)
            else:
                print("Aucun utilisateur trouvé.")