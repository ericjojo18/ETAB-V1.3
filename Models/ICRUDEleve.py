from abc import ABC, abstractmethod
from Models import Eleve
class ICRUDEleve(ABC):
    
    """
        interface CRUD  pour l'élève pour les classes abstract
    """
    @abstractmethod
    def ajouter(self, eleve) -> Eleve:
        pass

    @abstractmethod
    def modifier(self, eleve) -> Eleve:
        pass

    @abstractmethod
    def supprimer(self, eleve) -> bool:
        pass

    @abstractmethod
    def obtenirEleve(self) -> list:
        pass

    @abstractmethod
    def Obtenir(self,id) :
        pass
