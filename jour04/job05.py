import math

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius ** 2


rectangle1 = Rectangle(4, 5)

resultat_aire_rectangle = rectangle1.aire()

print(f"L'aire du rectangle est : {resultat_aire_rectangle}")

cercle1 = Cercle(3)

resultat_aire_cercle = cercle1.aire()

# Affichage du résultat en console
print(f"L'aire du cercle est : {resultat_aire_cercle}")