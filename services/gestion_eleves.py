# -*- coding: utf-8 -*-
#from Personne import Eleve
#from Models.Eleve import Eleve

from Models.Eleve import  Eleve
import datetime

class GestionEleve:
    
    #def __init__(self):
        #self.eleves = {}
        
    # Pour afficher le menu 
    def afficher_menu(self):
        while True:
            print("*" * 20)
            print("\nGESTION DES ÉLÈVES")
            print("*" * 20)
            print("\nMenu:")
            print("1: Ajouter un élève")
            print("2: Supprimer un élève")
            print("3: Modifier les informations de l'élève")
            print("4: Lister les élèves")
            print("5: Retour")
            print("0: Quitter")
            
            menu_choix = input("Choisissez une option: ")
            try:
                if menu_choix == '1':
                    self.ajouter_eleve()
                elif menu_choix == '2':
                    self.supprime_eleve()
                elif menu_choix == '3':
                    self.modifier_eleve()
                elif menu_choix == '4':
                    self.lister_eleve() 
                elif menu_choix == '5':
                    break
                elif menu_choix == '0':
                    break
                else:
                    print("Option non valide, veuillez réessayer.")
            except ValueError as e:
                print(f"Erreur: {e}")

    # Ajouter un élève
    def ajouter_eleve(self):
        try:
            
            nom = input("Entrez le nom: ")
            if not nom:
                raise ValueError("Le champ nom ne peut pas être vide.")
        
            prenom = input("Entrez le prénom: ")
            if not prenom:
                raise ValueError("Le champ prénom ne peut pas être vide.")
        
            dateNaissance = input("Entrez la date de naissance (21/10/2000): ")
            dateNaissance = datetime.datetime.strptime(dateNaissance, "%d-%m-%Y")
            if not dateNaissance:
                raise ValueError("Le champ date de naissance ne peut pas être vide.")
       
            ville = input("Entrez la ville: ")
            if not ville:
                raise ValueError("Le champ ville ne peut pas être vide.")
            
            telephone = input("Entrez la telephone: ")
            if not telephone:
                raise ValueError("Le champ ville ne peut pas être vide.")
        
            classe = input("Entrez la classe: ")
            if not classe:
                raise ValueError("Le champ classe ne peut pas être vide.")
            
            matricule = input("Entrez la matricule: ")
            if not matricule:
                raise ValueError("Le champ classe ne peut pas être vide.")
            
            eleve = Eleve(None,nom, prenom, ville, dateNaissance, telephone, classe,matricule)
            Eleve.ajouter(eleve)
        
            #eleve = Eleve(id, nom, prenom, dateNaissance, ville, classe, matricule)
        
            #self.eleves[id] = eleve
            print("\nÉlève ajouté avec succès")
        except ValueError as e:
            print(f"Erreur: {e}")

    # Supprimer un élève
    def supprime_eleve(self) :
        id = int(input("\nEntrez l'identifiant unique de l'élève à supprimer: "))
        Eleve.supprimer(id)
    
        print("\nÉlément supprimé avec succès")

    # Modifier les informations de l'élève
    def modifier_eleve(self ) :
        
    
        try:
            id = int(input("\nEntrez l'identifiant unique de l'élève à modifier: "))
            if not id:
                raise ValueError("L'identifiant ne peut pas être vide.")
            
    
            eleve = Eleve.Obtenir(id)
    
            while True:
                print("\n1: Modifier le nom")
                print("2: Modifier le prénom")
                print("3: Modifier la date de naissance (21/10/2000)")
                print("4: Modifier la ville")
                print("5: Modifier la classe")
                print("6: Modifier la matricule")
                print("7: Modifier l'identifiant")
                print("8: Retour")
                print("9: Accueil")
        
                menu_modify = input("Choisissez une option: ")    
        
                # Modifier le nom
                if menu_modify == '1':
                    new_nom = input("Entrez le nouveau nom: ") 
                    if not new_nom:
                        raise ValueError("Le champ nom ne peut pas être vide.")      
                    eleve.nom = new_nom
         
                # Modifier le prénom
                elif menu_modify == '2':
                    new_prenom = input("Entrez le nouveau prénom: ") 
                    if not new_prenom:
                        raise ValueError("Le champ prénom ne peut pas être vide.")        
                    eleve.prenom = new_prenom
            
                # Modifier la date de naissance 
                elif menu_modify == '3':
                    new_dateNaissance = input("Entrez la nouvelle date de naissance : ")   
                    if not new_dateNaissance:
                        raise ValueError("Le champ date de naissance ne peut pas être vide.")  
                    eleve.dateNaissance = new_dateNaissance 
            
                # Modifier la ville
                elif menu_modify == '4':
                    new_ville = input("Entrez la nouvelle ville : ")   
                    if not new_ville:
                        raise ValueError("Le champ ville ne peut pas être vide.")  
                    eleve.ville = new_ville
                
                # Modifier la classe
                elif menu_modify == '5':
                    new_classe = input("Entrez la nouvelle classe: ")   
                    if not new_classe:
                        raise ValueError("Le champ classe ne peut pas être vide.")  
                    eleve.classe = new_classe
                    
                elif menu_modify == '6':
                    new_matricule = input("Entrez la nouvelle classe: ")   
                    if not new_classe:
                        raise ValueError("Le champ classe ne peut pas être vide.")  
                    eleve.classe = new_matricule
            
                # Modifier l'identifiant    
                elif menu_modify == '7':
                    new_id = input("Entrez le nouvel identifiant: ")  
                    if not new_id:
                        raise ValueError("Le champ identifiant ne peut pas être vide.")  
                    self.eleves[new_id] = self.eleves.pop(id)
                    id = new_id
                elif menu_modify == '8':
                    break
                elif menu_modify == '9':
                    break
                else:
                    print("Option invalide. Veuillez réessayer.")
        except ValueError as e:
            print(f"Erreur: {e}")

    # Liste des élèves
    def lister_eleve(self):
        eleves = Eleve.obtenirEleve() 
        if eleves is not None:
            print("Liste des élèves :")
            for e in eleves:
                print(f"ID: {e[0]}, Nom : {e[1]}, Prénom : {e[2]}, Ville : {e[3]}, Date de Naissance : {e[4]}, "
                    f"Téléphone : {e[5]}, Classe : {e[6]}, Matricule : {e[7]}") 
                self.afficher_menu()
        else:
         print("Aucun élève trouvé.")
        
    # Obtenir le dernier élève ajouté
    