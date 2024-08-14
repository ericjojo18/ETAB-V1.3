from Models.Personne import Personne
#la classe Professeur qui herite des methodes et des propriétés de la classe personne en utilisant la fonction super()        
class Profeseur(Personne):
    def __init__(self, nom, prenom, ville, dateNaissance, vacant, matiereEnseigne, prochainCours,sujetProchaineReunion):
        super().__init__( nom, prenom, ville, dateNaissance)
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