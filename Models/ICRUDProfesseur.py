from abc import ABC, abstractmethod
from Models import Professeur
class ICRUDProfesseur(ABC):
   
    @abstractmethod
    def ajouter(self, professeur) -> Professeur:
        pass

    @abstractmethod
    def modifier(self, professeur) -> Professeur:
        pass

    @abstractmethod
    def supprimer(self, professeur) -> bool:
        pass


    @abstractmethod
    def obtenirProf(self) -> list:
        pass

    @abstractmethod
    def Obtenir(self,id) :
        pass
