from Auth import Authentification
from menu import MenuPrincipal

if __name__ == "__main__":
    Auth = Authentification()
    
    if Auth.connexion():
        menu = MenuPrincipal()
        menu.menuP()