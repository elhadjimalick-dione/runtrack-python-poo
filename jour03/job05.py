import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancerJeu(self):
        self.choisirNiveau()

        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 80
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 100
        elif self.niveau == 3:
            vie_joueur = 70
            vie_ennemi = 120
        else:
            print("Niveau non valide. Le jeu démarre au niveau 1 par défaut.")
            vie_joueur = 100
            vie_ennemi = 80

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

            print(f"\n{Jeu.getEtatPartie(joueur, ennemi)}\n")

            self.verifierSante(joueur)
            self.verifierSante(ennemi)

        print(f"{Jeu.getGagnant(joueur, ennemi)}")

    @staticmethod
    def getEtatPartie(joueur, ennemi):
        return f"{joueur.nom} - Vie : {joueur.vie} | {ennemi.nom} - Vie : {ennemi.vie}"

    @staticmethod
    def getGagnant(joueur, ennemi):
        if joueur.vie > 0:
            return f"{joueur.nom} a gagné !"
        elif ennemi.vie > 0:
            return f"{ennemi.nom} a gagné !"
        else:
            return "Match nul !"

    @staticmethod
    def verifierSante(personnage):
        if personnage.vie <= 0:
            print(f"{personnage.nom} n'a plus de vie.")

# Exécution du jeu
jeu = Jeu()
jeu.lancerJeu()