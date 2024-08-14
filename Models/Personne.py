# -*- coding: utf-8 -*-
import datetime
#definir la classe personne
class Personne:
    def __init__(self,id, nom, prenom, ville, dateNaissance, telephone):
         #Personne.__idUnique += 1
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__ville = ville 
        self.__dateNaissance = dateNaissance
        self.__telephone =  telephone
        
        #afficher les informations de la personne
    def __str__ (self):
        print(f"Id: {self.get_id}, Nom: {self.get_nom}, Prenom: {self.get_prenom}, ville: {self.get_ville}, date_naissance: {self.get_dateNaissance}")
        
    def ObteniAge(self):
        datePresent = datetime.date.today()
        dateNaissance = datetime.strptime(self.__dateNaissance, "%Y-%m-%d")
        age = datePresent.year - dateNaissance.year -((datePresent.month, dateNaissance.day) < (dateNaissance.month, dateNaissance.day))
        return age

    # Retourne l'identifiant unique de la personne 
    @property 
    def get_id(self):
        return self.__id

    # Retourne la date de naissance de la personne.
    @property 
    def get_date_naissance(self):
        return self.__dateNaissance

    # Retourne la ville de résidence de la personne.
    @property 
    def get_ville(self):
        return self.__ville

    # Retourne le prénom de la personne.
    @property 
    def get_prenom(self):
        return self.__prenom

    # Retourne le nom de la personne.
    @property
    def get_nom(self):
        return self.__nom    

    # Retourne le numéro de téléphone de la personne.
    @property
    def get_telephone(self):
        return self.__telephone    
    
    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_nom(self, nom):
        self.__nom = nom

    def set_ville(self, ville):
        self.__ville = ville

    def set_date_naissance(self, date_naissance):
        self.__dateNaissance = date_naissance   

    def set_telephone(self, telephone):
        self.__telephone = telephone    

        
        
#afficher les informations du professeur et la matiere
    def afficher_info(self):
        super().afficher_info()
        vacant_str = "Oui" if self.vacant else "Non"
        print(f"Vacant : {vacant_str}")
        
    
    def enseigner(self, matiereEnseigne: str) -> str:
        
        print(f"Enseigne la matière:{self.matiereEnseigne}")
       
    @classmethod 
    def preparerCours(self):
        
        
        print(f"Perarer le prochain cours:{self.prochainCours}")
        
    @classmethod 
    def preparerCours(self):
        super().enseigner()
        print(f"Doit assister à unne reunion:{self.sujetProchaineReunion}")
         
#la classe Eleve qui herite des methodes et des propriétés de la classe personne en utilisant la fonction super()        
class Eleve(Personne):
    def __init__(self, id, nom, prenom, ville, dateNaissance, classe, matricule):
        super().__init__(id, nom, prenom, ville, dateNaissance)
        self.classe =  classe
        self.matricule = matricule
        
        

#afficher les informations de l'élève et la classe      
    def afficher_info(self):
         super().afficher_info()
         print(f"classe:{self.classe}")

        