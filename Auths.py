from utilisateur import Utilisateur
class Authentification:
    def __init__(self):
        self.pseudo = "admin"
        self.motDePasse = "admin"
        
        
    def connexion(self):
        
        print("*" * 20)
        print("\nBienvenue dans l'application Etab v1.3\n")
        print("*" * 20)
        print("\nCONNEXION\n")
        
        try:
            pseudo = input("Pseudo: ")
            if not pseudo:
                 raise ValueError("l'identifiant ne peut pass etre vide")
             
            motDePasse = input("mot de passe: ")
            
            if not motDePasse:
                 raise ValueError("le mot de passe ne peut pass etre vide")
            
            if pseudo == self.pseudo and motDePasse == self.motDePasse:
                print("Connexion réussie")
                return True
            else:
                print("Connexion echoue, Veuillez réessayer")
                return False
                #utlisateur = Utlisateur(identifiant, mot_de_passe)
                #self.utilisateur.append(utlisateur)
        except ValueError as e:
            print(f"Erreur: {e}")
        