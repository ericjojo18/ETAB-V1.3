from abc import ABC, abstractmethod
class IEducation():
    def __init__(self, nom, matiereEnseignee, vacataire=True):
        self.nom = nom
        self.matiereEnseignee = matiereEnseignee
        self.vacataire = vacataire

    @abstractmethod
    def enseigner(self, matiere: str) -> str:
        return f"{self.nom} enseigne {matiere}."

    def preparerCours(self, cours: str) -> str:
        return f"{self.nom} prépare le cours de {cours}."

    def assisterReunion(self, sujet: str) -> str:
        return f"{self.nom} assiste à la réunion sur {sujet}."
