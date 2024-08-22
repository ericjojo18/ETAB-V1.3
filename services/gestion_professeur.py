# -*- coding: utf-8 -*-
#from Personne import Profeseur
from Models.Professeur import Professeur
import datetime
class GestionProf():
    
    
        
        
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
            print("5: Retour")
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
    def ajouter_prof(self):
        try:
            
            nom = input("Entrez votre nom: ")
            if not nom:
                raise ValueError("le champ nom ne peut pass etre vide")
        
            prenom = input("Entrez votre prénom: ")
            if not prenom:
                raise ValueError("le champ prenom ne peut pass etre vide")
            
            ville = input("Entrez votre ville: ")
            if not ville:
                raise ValueError("le champ ville ne peut pass etre vide")
        
            date_naissance = input("Entrez la date de naissance (21/10/2000): ")
            date_naissance = datetime.datetime.strptime(date_naissance, "%d/%m/%Y")
            if not date_naissance:
                raise ValueError("le champ date de naissance ne peut pass etre vide")
            
            telephone = input("Entrez la telephone: ")
            if not telephone:
                raise ValueError("Le champ telephone ne peut pas être vide.")
        
            vacant = str(input("Le poste est-il vacant ? (oui/non): "))
            if  vacant not in ['oui', 'non']:
                raise ValueError(" le champ poste vacant ne peut pass etre vide")
            vacant = True if vacant == 'oui' else False
            
            matiere_enseigne = input("Entrez votre matiere: ")
            if not matiere_enseigne:
                raise ValueError("le champ matiere ne peut pass etre vide")
            
            prochain_cours = input("Entrez votre prochain Cours: ")
            if not prochain_cours:
                raise ValueError("le champ prochainCours ne peut pass etre vide")
            
            sujet_prochaine_reunion = input("Entrez votre prochaines reunion: ")
            if not sujet_prochaine_reunion:
                raise ValueError("le champ prochainCours ne peut pass etre vide")
        
            prof = Professeur(id,nom, prenom, ville, date_naissance, 
                                    telephone, vacant, 
                                    matiere_enseigne, 
                                    prochain_cours, sujet_prochaine_reunion)

            Professeur.ajouter(prof)
            
            print("\nProfesseur ajoute avec succès")
        except ValueError as e:
            print(f"Erreur: {e}")

        #supprimer un professeur
    def supprime_prof(self ) :
        id = input("\nEntrez l'identifiant unique de l'élève à supprimer: ")
        
        Professeur.supprimer(id) 
        if not  Professeur.supprimer(id):
            print(f"L'utilisateur {id} n'existe pas.")
    
        print("\nÉlément supprimé avec succès")  
        
        ## Modifier les informations du professeur

    def modifier_prof(self):
                 
        
        try:
            id = int(input("Entrez l'identifiant du professeur à modifier: "))
            professeur = Professeur.Obtenir(id)
            
            if professeur:
                print(professeur)
                
                # Mise à jour des attributs
                new_date_naissance = input("Nouvelle date de naissance (JJ/MM/AAAA) : ") or professeur.get_date_naissance()
                if new_date_naissance:
                    try:
                        date_naissance_obj = datetime.datetime.strptime(new_date_naissance, "%d/%m/%Y")
                        new_date_naissance = date_naissance_obj.strftime("%Y-%m-%d")
                    except ValueError:
                        raise ValueError("La date de naissance doit être au format JJ/MM/AAAA.")
                
                new_ville = input("Nouvelle ville : ") or professeur.get_ville()
                new_prenom = input("Nouveau prénom : ") or professeur.get_prenom()
                new_nom = input("Nouveau nom : ") or professeur.get_nom()
                new_telephone = input("Nouveau téléphone : ") or professeur.get_telephone()
                new_vacant  = input("Nouvelle classe : ") or professeur.get_vacant ()
                new_matiere_enseigne = input("Nouveau matiere_enseigne : ") or professeur.get_matiere_enseigne()
                new_prochain_cours = input("Nouveau prochain_cours : ") or professeur.get_prochain_cours()
                new_prochaine_reunion  = input("Nouveau prochaine_reunion : ") or professeur.get_prochaine_reunion ()
        
                # Mettre à jour les attributs de l'objet
                professeur.set_date_naissance(new_date_naissance)
                professeur.set_ville(new_ville)
                professeur.set_prenom(new_prenom)
                professeur.set_nom(new_nom)
                professeur.set_telephone(new_telephone)
                professeur.set_vacant (new_vacant )
                professeur.set_matiere_enseigne(new_matiere_enseigne )
                professeur.set_prochain_cours(new_prochain_cours)
                professeur.set_prochaine_reunion(new_prochaine_reunion)
        
                # Appeler la méthode modifier de la classe
                if Professeur.modifier(professeur):
                    print("\nÉlève modifié avec succès")
                else:
                    print("Erreur lors de la modification de l'élève.")

            else:
                    print("Option invalide. Veuillez réessayer.")
        except ValueError as e:
            print(f"Erreur: {e}")
        
     #liste des professeurs
    def list_prof(self):
        professeurs = Professeur.obtenirProf()  # Assurez-vous que la méthode est correcte pour obtenir la liste des professeurs
        if professeurs:
           
            print("\nListe des professeurs :")
            for pr in professeurs:
                print(f"\nID: {pr.get_id()}, Nom : {pr.get_nom()}, Prénom : {pr.get_prenom()}, Ville : {pr.get_ville()}, "
                    f"Date de Naissance : {pr.get_date_naissance()}, Téléphone : {pr.get_telephone()}, "
                    f"Vacant : { pr.get_vacant() }, Matière enseignée : {pr.get_matiere_enseigne()}, "
                    f"Prochain cours : {pr.get_prochain_cours()}, Sujet de la prochaine réunion : {pr.get_sujet_prochaine_reunion()}")
                print("-" * 20)
            self.afficher_menu()
        else:
            print("Aucun professeur trouvé.")

            
        #Obtenir le dernier professeur ajouté

    