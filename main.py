# Document (nom, auteur, numPAge)
from abc import ABC
from operator import truediv


class Document(ABC):
    def __init__(self, nom, auteur):
        self.nom = nom
        self.auteur = auteur

    def __str__(self):
        return "[Document  " + self.nom + "   " + self.auteur + " ]"


# Livres (ISBN, annee)
class Livre(Document):
    def __init__(self, nom, auteur, ISBN, annee):
        super().__init__(nom, auteur)
        self.ISBN = ISBN
        self.annee = annee

# Adherent id, nom, prenom,
# identifiant unique ...

class Adherent:
    pass


# Emprunt (livre, adherent)

class Emprunt:
    pass


# Bibliotheque :
# liste de livre
# liste d'adherants
# liste d'emprunts
class Bibliotheque:
    listeLivres = []
    listeEmprunts = []
    listeAdherents = []

    def charger_livres_depuis_fichier(cls):
        pass

    @classmethod
    def afficher_liste_livres(cls):
        for l in cls.listeLivres:
            print(l)


# GestionFichier

# Menu
class Menu:
    @classmethod
    def afficherMenu(cls):
        print("***********************************************")
        print("*                                             *")
        print("*      Bienvenue à la bibliothèque LMN        *")
        print("*                                             *")
        print("***********************************************")
        print("**********           MENU            **********")
        print("*                                             *")
        print("* 1 Ajouter adhérent                          *")
        print("* 2 Supprimer adhérent                        *")
        print("* 3 Afficher tous les adhérents               *")
        print("* 4 Ajouter Document                          *")
        print("* 5 Supprimer Document                        *")
        print("* 6  Afficher tous les Documents              *")
        print("* 7  Ajouter Emprunt                          *")
        print("* 8  Retour d’un Emprunt                      *")
        print("* 9  Afficher tous les Emprunts               *")
        print("* 10  Quitter                                 *")
        print("*                                             *")
        print("***********************************************")
# Ajout adhérent
#


# Main

condition = True

while (condition):
    Menu.afficherMenu()
    reponse = int(input("Reponse : "))
    reponse = reponse.lower()
    if (reponse == "c"):
        condition = True
    elif (reponse == "q"):
        condition = False
    elif (reponse == "1"):
        # code pour ajouter un livre
        titre = input("titre : ")
        auteur = input("auteur : ")
        ISBN = input("ISBN : ")
        annee = input("annee : ")
        l = Livre(titre, auteur, ISBN, annee)
        Bibliotheque.listeLivres.append(l)
        Bibliotheque.afficher_liste_livres()
    else:
        print(" Seulement c et q sont acceptés")
        condition = True

