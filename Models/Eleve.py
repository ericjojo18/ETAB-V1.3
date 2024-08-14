#la classe Eleve qui herite des methodes et des propriétés de la classe personne en utilisant la fonction super()        
from Models.Personne import Personne
class Eleve(Personne):
    def __init__(self, nom:str, prenom:str, ville:str, dateNaissance, classe, matricule):
        super().__init__( nom, prenom, ville, dateNaissance)
        self.classe =  classe
        self.matricule = matricule 
        
        

#afficher les informations de l'élève et la classe      
    def afficher_info(self):
         super().afficher_info()
         print(f"classe:{self.classe}")
