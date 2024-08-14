# -*- coding: utf-8 -*-
from services.gestion_eleves import GestionEleve
from services.gestion_professeur import GestionProf
from services.gestion_utilisateur import GestionUtilisateur

#from services import GestionEleve, GestionProf, GestionUtilisateur
import time
    
class MenuPrincipal:   
    def __init__(self):
        # Enregistrer l'heure de début de la session lors de l'initialisation
        
        self.start_time = time.time()
        
    def menuP(self):
    
        while True:
            print("*" * 20)
            print("\nBienvenue dans l'application Etab v1.3\n")
            print("*" * 20)
            print("\nMenu: \n")
            print("1: Gestion des élèves")
            print("2: Gestion des professeurs")
            print("3: Gestion des utilisateurs")
            print("0: Quitter")
            
    
            menu_choice = input("Choisissez une option: ")
            try:
                if menu_choice == '1':
                    self.gestion_eleves()
                elif menu_choice == '2':
                   self.gestion_professeur()
                elif menu_choice == '3':
                   self.gestion_utilisateur()
                elif menu_choice == '0':
                    self.quitter()
                    #print("Au revoir")
                    break
                else:
                     print("Option non valide, veuillez réessayer.")
            except ValueError as e:
                print(f"Erreur: {e}")
            
    def gestion_eleves(self):
        gestion = GestionEleve()
        gestion.afficher_menu()
    
    def gestion_professeur(self):
        gestion = GestionProf()
        gestion.afficher_menu()
    
    def gestion_utilisateur(self):
        gestion = GestionUtilisateur()
        gestion.afficher_menu()
        
    def quitter(self):
        
        end = time.time()

        session = end - self.start_time 
        minutes, seconds = divmod(session, 60)
        print("Merci d'avoir utilisé l'application ETAB v1.3")
        print(f"Durée de la session : {int(minutes)} minutes et {int(seconds)} secondes")