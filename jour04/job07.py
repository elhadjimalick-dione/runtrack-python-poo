import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()
        self.main_joueur = []
        self.main_croupier = []

    def creer_paquet(self):
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def distribuer_cartes(self):
        self.main_joueur = [self.tirer_carte(), self.tirer_carte()]
        self.main_croupier = [self.tirer_carte(), self.tirer_carte()]

    def tirer_carte(self):
        return self.paquet.pop()

    def calculer_total(self, main):
        total = sum(carte.valeur for carte in main)
        nb_as = sum(1 for carte in main if carte.valeur == 11)

        while total > 21 and nb_as:
            total -= 10
            nb_as -= 1

        return total

    def joueur_peut_tirer(self):
        return input("Voulez-vous tirer une carte ? (oui/non) ").lower() == 'oui'

    def jouer(self):
        self.distribuer_cartes()

        while True:
            print(f"Votre main: {[carte.valeur for carte in self.main_joueur]}, Total: {self.calculer_total(self.main_joueur)}")
            print(f"Carte du croupier: [{self.main_croupier[0].valeur}]")

            if self.calculer_total(self.main_joueur) > 21:
                print("Vous avez dépassé 21. Vous avez perdu!")
                break

            if not self.joueur_peut_tirer():
                break

            self.main_joueur.append(self.tirer_carte())

        while self.calculer_total(self.main_croupier) < 17:
            self.main_croupier.append(self.tirer_carte())

        print(f"Votre main: {[carte.valeur for carte in self.main_joueur]}, Total: {self.calculer_total(self.main_joueur)}")
        print(f"Main du croupier: {[carte.valeur for carte in self.main_croupier]}, Total: {self.calculer_total(self.main_croupier)}")

        if self.calculer_total(self.main_joueur) > 21:
            print("Vous avez dépassé 21. Vous avez perdu!")
        elif self.calculer_total(self.main_joueur) > self.calculer_total(self.main_croupier):
            print("Vous avez gagné!")
        elif self.calculer_total(self.main_joueur) < self.calculer_total(self.main_croupier):
            print("Le croupier a gagné!")
        else:
            print("Égalité!")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer()