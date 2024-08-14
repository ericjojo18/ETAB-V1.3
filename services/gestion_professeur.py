# -*- coding: utf-8 -*-
#from Personne import Profeseur
from  Models.Professeur import Profeseur
from Models.ICRUDProfesseur import ICRUDProfesseur
class GestionProf:
    
    def __init__(self):
        self.professeurs = {}
        
        
        
        #pour afficher le menu 
    def afficher_menu(self):
        
        while True:
            print("*" * 20)
            print("\nGESTION DES PROFESSEURS")
            print("*" * 20)
            print("\nMenu:")
            print("1: Ajouter un professeur")
            print("2: Supprimer un professeur")
            print("3: Modifier les informations du professeur")
            print("4: Lister les professeurs")
            print("5: Obtenir le dernier professeurr ajouté")
            print("6: Retour")
            print("0: Quitter")
            
            menu_choix = input("Choisissez une option: ")
            try:
                if menu_choix == '1':
                    self.ajouter_prof()
                elif menu_choix == '2':
                    self.supprime_prof()
                elif menu_choix == '3':
                   self.modifier_prof()
                elif menu_choix == '4':
                    self.list_prof() 
                elif menu_choix == '5':
                    self.dernier_prof()
                elif menu_choix == '6':
                    break
                elif menu_choix =='0':
                    break
                else:
                    print("Option non valide, veuillez réessayer.")
            except ValueError as e:
                print(f"Erreur: {e}")
    
        #la fonction pour ajouter un professeur
    def ajouter_prof(self) -> bool:
        try:
            id = input("Entrez votre identifiant: ")
            if not id:
                raise ValueError("le champ identifiant ne peut pass etre vide")
        
            nom = input("Entrez votre nom: ")
            if not nom:
                raise ValueError("le champ nom ne peut pass etre vide")
        
            prenom = input("Entrez votre prénom: ")
            if not prenom:
                raise ValueError("le champ prenom ne peut pass etre vide")
        
            dateNaissance = input("Entrez la date de naissance (21/10/2000): ")
            if not dateNaissance:
                raise ValueError("le champ date de naissance ne peut pass etre vide")
       
            ville = input("Entrez votre ville: ")
            if not ville:
                raise ValueError("le champ ville ne peut pass etre vide")
        
            vacant = str(input("Le poste est-il vacant ? (oui/non): "))
            if  vacant not in ['oui', 'non']:
                raise ValueError(" le champ poste vacant ne peut pass etre vide")
            vacant = True if vacant == 'oui' else False
            
            matiereEnseigne = input("Entrez votre matiere: ")
            if not matiereEnseigne:
                raise ValueError("le champ matiere ne peut pass etre vide")
            
            prochainCours = input("Entrez votre prochain Cours: ")
            if not prochainCours:
                raise ValueError("le champ prochainCours ne peut pass etre vide")
            
            sujetProchaineReunion = input("Entrez votre prochainCours: ")
            if not sujetProchaineReunion:
                raise ValueError("le champ prochainCours ne peut pass etre vide")
        
            professeur = Profeseur(id,nom, prenom, dateNaissance, ville, vacant, matiereEnseigne, prochainCours,  sujetProchaineReunion)
        
            #self.professeurs.append(professeur)
            self.professeurs[id] = professeur
            print("\nProfesseur ajoute avec succès")
        except ValueError as e:
            print(f"Erreur: {e}")

        #supprimer un professeur
    def supprime_prof(self, ) -> bool:
        id = input("\nEntrez l'identifiant unique de l'élève à supprimer: ")
        
        try:
            if not id:
                raise ValueError("l'identifiant ne peut pas etre vide.")
            if id in self.professeurs:
                del self.professeurs[id]
                #self.professeurs.remove(id)
                print("Professeur supprimé avec succès.")
            else:
                print("Aucun Professeur trouvé avec cet identifiant.")
        except ValueError as e:
            print(f"Erreur: {e}")  
        
        ## Modifier les informations du professeur

    def modifier_prof(self, professeur) -> bool:
        id = input("\nEntrez l'identifiant unique du professeur à modifier: ")         
        
        try:
            #verifier si l'id existe
            if not id:
                raise ValueError("l'identifiant ne peut pas etre vide.")
            if id not in self.professeurs:
                print("Aucun professeur trouvé avec cet identifiant.")
                #return
        
            professeur = self.professeurs[id]
        
            while True:
                print("\n1: Modifier le nom")
                print("2: Modifier le prénom")
                print("3: Modifier la date de naissance (21/10/2000)")
                print("4: Modifier la ville")
                print("5: Modifier le poste vacant")
                print("6: Modifier la matiere")
                print("7:Modifier prochain cour")
                print("8:Modifier sujet Prochain Cours")
                print("9: Modifier l'identifiant")
                print("10: Retour")
                print("11: Accueil")
            
                menu_modify = input("Choisissez une option: ")    
            
                #modifier le nom
                if menu_modify == '1':
                    new_nom = input("Entrez le nouveau nom: ") 
                    if not new_nom:
                        raise ValueError("l'identifiant ne peut pas etre vide.")      
                    professeur.nom = new_nom
            
                #modifier le prénom
                elif menu_modify == '2':
                    new_prenom = input("Entrez le nouveau prénom: ") 
                    if not new_prenom:
                        raise ValueError("l'identifiant ne peut pas etre vide.")        
                    professeur.prenom = new_prenom
                
                    #modifier la date de naissance 
                elif menu_modify == '3':
                    new_dateNaissance  = input("Entrez le nouvel date de naissance : ")   
                    if not new_dateNaissance :
                        raise ValueError("l'identifiant ne peut pas etre vide.")  
                    professeur.dateNaissance  = new_dateNaissance 
                
                    #modifier la ville
                elif menu_modify == '4':
                    new_ville  = input("Entrez le nouvel ville : ")   
                    if not new_ville :
                        raise ValueError("la ville ne peut pas etre vide.")  
                    professeur.ville  = new_ville
                    
                    #modifier la vacant
                elif menu_modify == '5':
                    new_vacant  = input("Entrez la vacant : ")   
                    if not new_vacant in ['oui', 'non']:
                        raise ValueError("la vacant ne peut pas etre vide.")  
                    professeur.vacant  = new_vacant
                    new_vacant = True if new_vacant == 'oui' else False
                    
                    
                
                    
                elif menu_modify == '6':
                    new_matiereEnseigne  = input("Entrez la vacant : ")   
                    if not new_matiereEnseigne  :
                        raise ValueError("la vacant ne peut pas etre vide.")  
                    professeur.matiereEnseigne  = new_matiereEnseigne 
                    
                elif menu_modify == '7':
                    new_prochainCours  = input("Entrez la vacant : ")   
                    if not new_prochainCours :
                        raise ValueError("la vacant ne peut pas etre vide.")  
                    professeur.prochainCours = new_prochainCours
                    
                elif menu_modify == '8':
                    new_sujetProchaineReunion  = input("Entrez la vacant : ")   
                    if not new_sujetProchaineReunion :
                        raise ValueError("la vacant ne peut pas etre vide.")  
                    professeur.sujetProchaineReunion  = new_sujetProchaineReunion
                
                #modifier l'identifiant    
                elif menu_modify == '9':
                    new_id = input("Entrez le nouvel identifiant: ")  
                    if not new_id:
                        raise ValueError("l'identifiant ne peut pas etre vide.")       
                    self.professeur[new_id] = self.professeur.pop(id)
                    id = new_id
                elif menu_modify == '10':
                    break
                elif menu_modify == '11':
                    
                    break
                else:
                    print("Option invalide. Veuillez réessayer.")
        except ValueError as e:
            print(f"Erreur: {e}")
        
     #liste des professeurs
    def list_prof(self) -> list:
        if not self.professeurs:
            print("Aucun professeur trouvé.")
            return
        print("\nListe des élèves :")
        for professeur in self.professeurs.values():
            print("\nID:", professeur.id)
            print("Nom:", professeur.nom)
            print("Prénom:", professeur.prenom)
            print("Date de naissance:", professeur.dateNaissance)
            print("ville:", professeur.ville)
            print("vacant:", professeur.vacant)
            print("matiereEnseigne:", professeur.matiereEnseigne)
            print("prochainCour:", professeur.prochainCours)
            print("sujetProchaineReunion:", professeur.sujetProchaineReunion)

            print("-" * 20) 
            
        #Obtenir le dernier professeur ajouté

    def dernier_prof(self) -> 'Profeseur':
        #if self.professeurs:
        # print(self.professeurs[-1])
        #else:
            #print("Aucun professeur trouvé.")
            
            if self.professeurs:
                dernier = next(reversed(self.professeurs.values()))
                print("\nDernier élève ajouté :")
                print("ID:", dernier.id)
                print("Nom:", dernier.nom)
                print("Prénom:", dernier.prenom)
                print("Date de naissance:", dernier.dateNaissance)
                print("Ville:", dernier.ville)
                print("vacant:", dernier.vacant)
                print("matiereEnseigne:", dernier.matiereEnseigne)
                print("prochainCour:", dernier.prochainCours)
                print("sujetProchaineReunion:", dernier.sujetProchaineReunion)
            else:
                print("Aucun professeur trouvé.")
        
