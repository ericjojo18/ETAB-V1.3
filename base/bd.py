from mysql.connector import Error
import mysql.connector
import bcrypt
import time

class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._connection = None
        return cls._instance
    
    def create_connection(self):
        if self._connection is None:
            try:
                self._connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='etab_db',
                    unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock',
                    port='8889'
                )
                if self._connection.is_connected():
                    print("\033[0;92mCONNECTION REUSSIE A LA BASE DE DONNEE\033[0m")
                return self._connection
            except Error as e:
                print(f"Erreur de connexion: {e}")
                return None
        return self._connection
    
    def close_connection(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()
            self._connection = None
            print("Connexion à la base de donnée ferme")
            
    
def create_database_and_tables(curseur):
        """Crée la base de données et les tables nécessaires."""
        curseur.execute("CREATE DATABASE IF NOT EXISTS etab_db;")
        curseur.execute("USE etab_db;")
        
        tables = [
            """
            CREATE TABLE IF NOT EXISTS utilisateurs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                pseudo VARCHAR(50) NOT NULL UNIQUE,
                mot_de_passe VARCHAR(255) NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS eleves (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(50) NOT NULL,
                prenom VARCHAR(50) NOT NULL,
                ville VARCHAR(100) NOT NULL,
                date_naissance DATE NOT NULL,
                telephone VARCHAR(50) NOT NULL,
                classe VARCHAR(50),
                matricule VARCHAR(50) UNIQUE
                
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS professeurs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(50) NOT NULL,
                prenom VARCHAR(50) NOT NULL,
                ville VARCHAR(100) NOT NULL,
                date_naissance DATE NOT NULL,
                telephone VARCHAR(50) NOT NULL,
                vacant BOOLEAN,
                matiere_enseigne VARCHAR(100),
                prochain_cours VARCHAR(100),
                sujet_prochaine_reunion VARCHAR(100)
                
            );
            """
        ]
        
        for table in tables:
            curseur.execute(table)
   
def setup_admin_user(curseur):
        """Vérifie et ajoute l'utilisateur administrateur si nécessaire."""
        pseudo_admin = 'admin'
        mot_de_passe_admin = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())

        curseur.execute("SELECT * FROM utilisateurs WHERE pseudo = %s", (pseudo_admin,))
        if curseur.fetchone() is None:
            curseur.execute("INSERT INTO utilisateurs (pseudo, mot_de_passe) VALUES (%s, %s);", (pseudo_admin, mot_de_passe_admin))
def main():
    db = DatabaseConnection()
    connection = db.create_connection() # Connection à la BD
    if connection.is_connected():
            print("\033[0;92mCONNECTION REUSSIE A LA BASE DE DONNEE\033[0m")
    else:
            print("\033[0;91m ECHEC DE CONNECTION A LA BASE DE DONNEE\033[0m")

    if connection: # Si la connection reussie
        try:
            curseur = connection.cursor() 
            create_database_and_tables(curseur)
            time.sleep(1)
            print("\033[0;92m\nGENERATION DES TABLES DANS LA BD\033[0m")
            setup_admin_user(curseur) # admin par defaut 
            time.sleep(1)
            print("\033[0;92m\nAJOUT DE L'ADMIN PAR DEFAUT\033[0m")
            connection.commit() # Validation des changements et mise à jour dans la BD
        except Error as e:
            print(f"Erreur!! {e}")
            connection.rollback() # Si il y'a une erreur dans les requetes revenir au dernier enregistrement
        finally:
            if connection.is_connected():
                curseur.close() # Fermeture de du curseur de requette
                db.close_connection() # Fermeture de la connexion

if __name__ == "__main__":
    main()