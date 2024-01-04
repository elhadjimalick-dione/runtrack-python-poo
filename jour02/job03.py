class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def is_disponible(self):
        return self.__disponible

    
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    
    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Erreur : Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Erreur : Le livre n'a pas été emprunté.")


mon_livre = Livre("Titre du Livre", "Auteur du Livre", 300)


print("Le livre est disponible :", mon_livre.verification())


mon_livre.emprunter()


print("Le livre est disponible :", mon_livre.verification())

mon_livre.rendre()

# Vérifier une dernière fois
print("Le livre est disponible :", mon_livre.verification())