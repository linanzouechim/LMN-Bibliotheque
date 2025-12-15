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
# --------- Bibliothèque ----------
class Bibliotheque:
    # listes en mémoire
    liste_livres: list[Livre] = []
    liste_emprunts: list[Emprunt] = []
    liste_adherents: list[Adherent] = []

    # noms des fichiers CSV
    FICHIER_ADHERENTS = "adherents.csv"
    FICHIER_LIVRES = "biblio.csv"
    FICHIER_EMPRUNTS = "emprunts.csv"

    # ---- Méthodes internes de recherche ----
    @classmethod
    def trouver_adherent_par_id(cls, identifiant: int) -> Adherent | None:
        for a in cls.liste_adherents:
            if a.identifiant == identifiant:
                return a
        return None

    # ---- Gestion des adhérents ----
    @classmethod
    def ajouter_adherent(cls, nom: str, prenom: str) -> None:
        if cls.liste_adherents:
            nouvel_id = max(a.identifiant for a in cls.liste_adherents) + 1
        else:
            nouvel_id = 1
        adherent = Adherent(nouvel_id, nom, prenom)
        cls.liste_adherents.append(adherent)
        cls.sauvegarder_adherents()
        print("Adhérent ajouté :", adherent)

    @classmethod
    def supprimer_adherent(cls, identifiant: int) -> None:
        adherent = cls.trouver_adherent_par_id(identifiant)
        if adherent is None:
            print("Adhérent introuvable.")
            return

        # vérifier s'il a des emprunts en cours
        for e in cls.liste_emprunts:
            if e.adherent_id == identifiant and e.date_retour is None:
                print("Impossible de supprimer : l'adhérent a des emprunts en cours.")
                return

        cls.liste_adherents.remove(adherent)
        cls.sauvegarder_adherents()
        print("Adhérent supprimé.")

    @classmethod
    def afficher_adherents(cls) -> None:
        if not cls.liste_adherents:
            print("Aucun adhérent.")
            return
        for a in cls.liste_adherents:
            print(a)

    # ---- Gestion fichiers CSV ----
    @classmethod
    def charger_adherents(cls) -> None:
        """Charge les adhérents depuis le fichier CSV"""
        cls.liste_adherents = []
        if not os.path.exists(cls.FICHIER_ADHERENTS):
            return
        try:
            with open(cls.FICHIER_ADHERENTS, newline="", encoding="utf-8") as f:
                lecteur = csv.reader(f)
                for ligne in lecteur:
                    if len(ligne) < 3:  # Ignorer les lignes vides ou incomplètes
                        continue
                    identifiant, nom, prenom = ligne[0], ligne[1], ligne[2]
                    cls.liste_adherents.append(Adherent(int(identifiant), nom, prenom))
        except Exception as e:
            print(f"Erreur lors du chargement des adhérents : {e}")

    @classmethod
    def sauvegarder_adherents(cls) -> None:
        """Sauvegarde la liste des adhérents dans le fichier CSV"""
        try:
            with open(cls.FICHIER_ADHERENTS, "w", newline="", encoding="utf-8") as f:
                ecrivain = csv.writer(f)
                for a in cls.liste_adherents:
                    ecrivain.writerow([a.identifiant, a.nom, a.prenom])
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des adhérents : {e}")
    # ---- Méthodes internes de recherche ----
    @classmethod
    def trouver_livre_par_isbn(cls, isbn: str) -> Livre | None:
        for l in cls.liste_livres:
            if l.isbn == isbn:
                return l
        return None

    # ---- Gestion des livres ----
    @classmethod
    def ajouter_livre(cls, titre: str, auteur: str, isbn: str, annee: str) -> None:
        if cls.trouver_livre_par_isbn(isbn):
            print("Un livre avec cet ISBN existe déjà.")
            return
        livre = Livre(titre, auteur, isbn, annee, True)
        cls.liste_livres.append(livre)
        cls.sauvegarder_livres()
        print("Livre ajouté :", livre)

    @classmethod
    def supprimer_livre(cls, isbn: str) -> None:
        livre = cls.trouver_livre_par_isbn(isbn)
        if livre is None:
            print("Livre introuvable.")
            return

        if not livre.disponible:
            print("Impossible de supprimer : livre actuellement emprunté.")
            return

        cls.liste_livres.remove(livre)
        cls.sauvegarder_livres()
        print("Livre supprimé.")

    @classmethod
    def afficher_liste_livres(cls) -> None:
        if not cls.liste_livres:
            print("Aucun livre.")
            return
        for l in cls.liste_livres:
            print(l)

    # ---- Gestion fichiers CSV ----
    @classmethod
    def charger_livres(cls) -> None:
        """Charge les livres depuis le fichier CSV"""
        cls.liste_livres = []
        if not os.path.exists(cls.FICHIER_LIVRES):
            return
        try:
            with open(cls.FICHIER_LIVRES, newline="", encoding="utf-8") as f:
                lecteur = csv.reader(f)
                for ligne in lecteur:
                    if len(ligne) < 4:  # Ignorer les lignes vides ou incomplètes
                        continue
                    titre, auteur, isbn, annee = ligne[0], ligne[1], ligne[2], ligne[3]
                    disponible = ligne[4].lower() == "true" if len(ligne) > 4 else True
                    cls.liste_livres.append(Livre(titre, auteur, isbn, annee, disponible))
        except Exception as e:
            print(f"Erreur lors du chargement des livres : {e}")

    @classmethod
    def sauvegarder_livres(cls) -> None:
        """Sauvegarde la liste des livres dans le fichier CSV"""
        try:
            with open(cls.FICHIER_LIVRES, "w", newline="", encoding="utf-8") as f:
                ecrivain = csv.writer(f)
                for l in cls.liste_livres:
                    ecrivain.writerow([l.nom, l.auteur, l.isbn, l.annee, str(l.disponible)])
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des livres : {e}")
