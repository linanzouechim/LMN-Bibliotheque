from abc import ABC
from datetime import date
import csv
import os


# --------- Classes de base ----------
class Document(ABC):
    def __init__(self, nom: str, auteur: str):
        self.nom = nom
        self.auteur = auteur

    def __str__(self) -> str:
        return f"[Document {self.nom} - {self.auteur}]"


class Livre(Document):
    """Livre (ISBN, année, disponible ou non)"""

    def __init__(self, nom: str, auteur: str, isbn: str, annee: str, disponible: bool = True):
        super().__init__(nom, auteur)
        self.isbn = isbn
        self.annee = annee
        self.disponible = disponible

    def __str__(self) -> str:
        dispo = "disponible" if self.disponible else "non disponible"
        return f"[Livre {self.nom} - {self.auteur} - {self.isbn} - {self.annee} - {dispo}]"


class Adherent:
    """Adhérent (id, nom, prénom)"""

    def __init__(self, identifiant: int, nom: str, prenom: str):
        self.identifiant = identifiant
        self.nom = nom
        self.prenom = prenom

    def __str__(self) -> str:
        return f"[Adherent {self.identifiant} - {self.nom} {self.prenom}]"


class Emprunt:
    """Emprunt (adherent, livre, dates)"""

    def __init__(self, adherent_id: int, isbn_livre: str, date_emprunt: date, date_retour: date | None = None):
        self.adherent_id = adherent_id
        self.isbn_livre = isbn_livre
        self.date_emprunt = date_emprunt
        self.date_retour = date_retour

    def prolongerDateRetour(self, nb_jours: int) -> None:
        if self.date_retour is None:
            self.date_retour = date.today()
        self.date_retour = self.date_retour.fromordinal(self.date_retour.toordinal() + nb_jours)

    def __str__(self) -> str:
        retour = self.date_retour.isoformat() if self.date_retour else "non retourné"
        return (
            f"[Emprunt adherent={self.adherent_id}, "
            f"livre={self.isbn_livre}, "
            f"date_emprunt={self.date_emprunt.isoformat()}, "
            f"date_retour={retour}]"
        )


# --------- Menu ----------
class Menu:
    @classmethod
    def afficher_menu(cls) -> None:
        print("***********************************************")
        print("*         Bienvenue à votre bibliothèque      *")
        print("*                Faites un choix :            *")
        print("***********************************************")
        print("* 1  Ajouter adhérent                        *")
        print("* 2  Supprimer adhérent                      *")
        print("* 3  Afficher tous les adhérents             *")
        print("* 4  Ajouter document                        *")
        print("* 5  Supprimer document                      *")
        print("* 6  Afficher tous les documents             *")
        print("* 7  Ajouter emprunt                         *")
        print("* 8  Retour d'un emprunt                     *")
        print("* 9  Afficher tous les emprunts              *")
        print("* Q  Quitter                                 *")
        print("***********************************************")
