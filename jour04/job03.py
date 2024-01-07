class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    
    def get_hauteur(self):
        return self.__hauteur

    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur


rectangle1 = Rectangle(5, 8)

# Accès aux attributs et utilisation des méthodes
print("Longueur du rectangle : ", rectangle1.get_longueur())
print("Largeur du rectangle : ", rectangle1.get_largeur())
print("Périmètre du rectangle : ", rectangle1.perimetre())
print("Surface du rectangle : ", rectangle1.surface())


rectangle1.set_longueur(10)
rectangle1.set_largeur(6)

# Vérification des modifications
print("\nAprès modification :")
print("Longueur du rectangle : ", rectangle1.get_longueur())
print("Largeur du rectangle : ", rectangle1.get_largeur())
print("Périmètre du rectangle : ", rectangle1.perimetre())
print("Surface du rectangle : ", rectangle1.surface())


parallelepipede1 = Parallelepipede(4, 6, 3)

# Utilisation des méthodes de la classe Parallelepipede
print("\nVolume du parallélépipède : ", parallelepipede1.volume())