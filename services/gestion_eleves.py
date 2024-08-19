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
        
            ville = input("Entrez la ville: ")
            if not ville:
                raise ValueError("Le champ ville ne peut pas être vide.")
            
            date_naissance = input("Entrez la date de naissance (21/10/2000): ")
            
            date_naissance= datetime.datetime.strptime(date_naissance, "%d/%m/%Y")
            if not date_naissance:
                raise ValueError("Le champ date de naissance ne peut pas être vide.")
            
            telephone = input("Entrez la telephone: ")
            if not telephone:
                raise ValueError("Le champ ville ne peut pas être vide.")
        
            classe = input("Entrez la classe: ")
            if not classe:
                raise ValueError("Le champ classe ne peut pas être vide.")
            
            matricule = input("Entrez la matricule: ")
            if not matricule:
                raise ValueError("Le champ classe ne peut pas être vide.")
            
            eleve = Eleve(None,nom, prenom, ville, date_naissance, telephone, classe, matricule)
            Eleve.ajouter(eleve)
        
            print("\nÉlève ajouté avec succès")
        except ValueError as e:
            print(f"Erreur: {e}")

    # Supprimer un élève
    def supprime_eleve(self) :
        id = int(input("\nEntrez l'identifiant unique de l'élève à supprimer: "))
        
        Eleve.supprimer(id)
        if not Eleve.supprimer(id):
            print(f"L'utilisateur {id} n'existe pas.")
    
        print("\nÉlément supprimé avec succès")

    # Modifier les informations de l'élève
    def modifier_eleve(self):
        try:
            id = int(input("Entrez l'identifiant de l'élève à modifier: "))
            eleve = Eleve.Obtenir(id)
            
            if eleve:
                print(eleve)
                
                # Mise à jour des attributs
                new_date_naissance = input("Nouvelle date de naissance (JJ/MM/AAAA) : ") or eleve.get_date_naissance()
                if new_date_naissance:
                    try:
                        date_naissance_obj = datetime.datetime.strptime(new_date_naissance, "%d/%m/%Y")
                        new_date_naissance = date_naissance_obj.strftime("%Y-%m-%d")
                    except ValueError:
                        raise ValueError("La date de naissance doit être au format JJ/MM/AAAA.")
                
                new_ville = input("Nouvelle ville : ") or eleve.get_ville()
                new_prenom = input("Nouveau prénom : ") or eleve.get_prenom()
                new_nom = input("Nouveau nom : ") or eleve.get_nom()
                new_telephone = input("Nouveau téléphone : ") or eleve.get_telephone()
                new_classe = input("Nouvelle classe : ") or eleve.get_classe()
                new_matricule = input("Nouveau matricule : ") or eleve.get_matricule()
        
                # Mettre à jour les attributs de l'objet
                eleve.set_date_naissance(new_date_naissance)
                eleve.set_ville(new_ville)
                eleve.set_prenom(new_prenom)
                eleve.set_nom(new_nom)
                eleve.set_telephone(new_telephone)
                eleve.set_classe(new_classe)
                eleve.set_matricule(new_matricule)
        
                # Appeler la méthode modifier de la classe
                if Eleve.modifier(eleve):
                    print("\nÉlève modifié avec succès")
                else:
                    print("Erreur lors de la modification de l'élève.")
            else:
                print("Élève non trouvé.")
        except ValueError as e:
            print(f"Erreur: {e}")



    # Liste des élèves
    def lister_eleve(self):
        eleves = Eleve.obtenirEleve()  # Assurez-vous que cette méthode retourne une liste d'objets Eleve
        if eleves:
            print("Liste des élèves :")
            for e in eleves:
                # Utilisez les méthodes d'accès définies dans la classe Eleve
                print(f"ID: {e.get_id()}, Nom : {e.get_nom()}, Prénom : {e.get_prenom()}, Ville : {e.get_ville()}, "
                    f"Date de Naissance : {e.get_date_naissance()}, Téléphone : {e.get_telephone()}, "
                    f"Classe : {e.get_classe()}, Matricule : {e.get_matricule()}")
            self.afficher_menu()
        else:
            print("Aucun élève trouvé.")

        
    # Obtenir le dernier élève ajouté
    