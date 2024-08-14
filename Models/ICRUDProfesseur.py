from abc import ABC, abstractmethod
from Models.Professeur import Profeseur
class ICRUDProfesseur(ABC):
    @abstractmethod
    def ajouter(self, profeseur) -> 'Profeseur':
        pass

    @abstractmethod
    def modifier(self, profeseur) -> 'Profeseur':
        pass

    @abstractmethod
    def supprime(self, profeseur) -> bool:
        pass

    @abstractmethod
    def dernier_prof(self, identifiant) -> 'Profeseur':
        pass

    @abstractmethod
    def list_prof(self) -> list:
        pass
