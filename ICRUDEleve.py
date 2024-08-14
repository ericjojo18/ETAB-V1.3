from abc import ABC, abstractmethod
from Models.Personne import Eleve
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
    def supprime(self, eleve) -> bool:
        pass

    @abstractmethod
    def obtenir(self, identifiant) -> 'Eleve':
        pass

    @abstractmethod
    def Obtenir(self) -> list:
        pass
