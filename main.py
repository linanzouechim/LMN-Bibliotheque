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
    def __init__(self):
        super().__init__(nom, auteur, disponibilite)
        self.ISBN = ISBN
        self.annee = annee
        self.disponibilite = disponibilite

# class BD
class BD(Volume):
    def __init__(self, dessinateur):
        self.dessinateur = dessinateur

# class Dictionnaire
class Dictionnaire(Volume):


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
    listeDocuments = []
    listeLivres = []
    listeEmprunts = []
    listeAdherents = []

    def charger_livres_depuis_fichier(cls):
        pass

# méthode ajouter document
    def  ajouter_document(self):

# méthode ajouter adhérent
    def ajoiuter_adherent(self):


# méthode supprimer adhérent
    def  supprimmer_adherent(self):

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
        print("* 10 Quitter                                  *")
        print("*                                             *")
        print("***********************************************")
# Ajout adhérent
#


# Main

condition = True

while (condition):
    Menu.afficherMenu()
    reponse = int(input("Reponse : "))
    if (reponse == 1):
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

