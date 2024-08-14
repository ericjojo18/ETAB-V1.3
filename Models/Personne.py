# -*- coding: utf-8 -*-
#definir la classe personne
class Personne:
    def __init__(self,id, nom, prenom, ville, dateNaissance, telephone) :
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__ville = ville 
        self.__dateNaissance  = dateNaissance
        self.__telephone =  telephone
        
        #afficher les informations de la personne
    def __str__ (self):
        print(f"Id: {self.id}, Nom: {self.nom}, Prenom: {self.prenom}, ville: {self.ville}, dateNaissance: {self.dateNaissance}")
        
#la classe Professeur qui herite des methodes et des propriétés de la classe personne en utilisant la fonction super() 

@property
       
class Profeseur(Personne):
    def __init__(self, id, nom, prenom, ville, dateNaissance, vacant, matiereEnseigne, prochainCours,sujetProchaineReunion):
        super().__init__(id, nom, prenom, ville, dateNaissance)
        self.vacant = vacant
        self.matiereEnseigne = matiereEnseigne
        self.prochainCours = prochainCours
        self.sujetProchaineReunion = sujetProchaineReunion
        
        
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

        