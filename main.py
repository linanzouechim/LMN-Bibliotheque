# Document (nom, auteur, numPAge)
from abc import ABC
from operator import truediv

# class Document
class Document(ABC):
    def __init__(self, titre):
        self.titre = titre

    def __str__(self):
        return "[Document  " + self.nom + "   " + self.auteur + " ]"



# class Journal
class Journal(Document):

    def __init__(self, date_parution):
        self.date_parution = date_parution

# class volume
class Volume(Document):
    def __init__(self, nom_auteur):
        self.nom_auteur = nom_auteur

# class Livres (ISBN, annee)
class Livre(Volume):
    def __init__(self, nom, auteur, disponibilite):
        self.nom = nom
        self.auteur = auteur
        self.disponibilite = disponibilite

# class BD
class BD(Volume):
    def __init__(self, dessinateur):
        self.dessinateur = dessinateur

# class Dictionnaire
class Dictionnaire(Volume):
    pass


# class Adherent
class Adherent:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom




# class Emprunt (livre, adherent)
class Emprunt:
    def __init__(self, livre, adherent, date_emprunt, date_retour):
        self.date_emprunt = date_emprunt
        self.date_retour = date_retour



# Bibliotheque :
# liste de livre
# liste d'adherants
# liste d'emprunts
class Bibliotheque:

    liste_adherents: list[Adherent]
    listeAdherents = []

    # noms des fichiers CSV
    FICHIER_ADHERENTS = "adherents.csv"


    def charger_livres_depuis_fichier(cls):
        pass

# méthode ajouter document
    def  ajouter_document(self):
        pass

# méthode ajouter adhérent
    @classmethod
    def ajoiuter_adherent(cls,nom: str, prenom: str):
       f - open(FICHIER_ADHERENTS, "a")


# méthode supprimer adhérent
    def  supprimmer_adherent(self):
        pass

    @classmethod
    def afficher_liste_livres(cls):
        for l in cls.listeLivres:
            print(l)

# c
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
        print("* 6 Afficher tous les Documents               *")
        print("* 7 Ajouter Emprunt                           *")
        print("* 8 Retour d’un Emprunt                       *")
        print("* 9 Afficher tous les Emprunts                *")
        print("* Q Quitter                                  *")
        print("*                                             *")
        print("***********************************************")
# Ajout adhérent
#


# Main

condition = True

while (condition):
    Menu.afficherMenu()
    reponse = input("Faites un choix : ").lower()
# 1 Ajouter adhérent
    if (reponse == "1"):
        condition = False
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        Bibliotheque.ajouter_adherent(nom, prenom)


# 2 Supprimer adhérent
    elif (reponse == "2"):
        condition = False
# 3 Afficher tous les adhérents
    elif (reponse == "3"):
        condition = False
# 4 Ajouter Document
    elif (reponse == "4"):
        condition = False
# 5 Supprimer Document
    elif (reponse == "5"):
        condition = False
# 6 Afficher tous les Documents
    elif (reponse == "6"):
        condition = False
# 7 Ajouter Emprunt
    elif (reponse == "7"):
        condition = False
# 8 Retour d’un Emprunt
    elif (reponse == "8"):
        condition = False
# 9 Afficher tous les Emprunts
    elif (reponse == "9"):
        condition = False
# 10 Quitter
    elif (reponse == "10"):
        condition = False
    elif (reponse == "8"):
        # code pour ajouter un livre
        titre = input("titre : ")
        auteur = input("auteur : ")
        ISBN = input("ISBN : ")
        annee = input("annee : ")
        l = Livre(titre, auteur, ISBN, annee)
        Bibliotheque.listeLivres.append(l)
        Bibliotheque.afficher_liste_livres()
    else:
        print(" Seulement 1 et 10 sont acceptés")
        condition = True

