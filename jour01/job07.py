class Personnage:
    def __init__(self, x=0, y=0, plateau_size=(10, 10)):
        self.x = x
        self.y = y
        self.plateau_size = plateau_size

    def gauche(self):
        if self.x > 0:
            self.x -= 1

    def droite(self):
        if self.x < self.plateau_size[0] - 1:
            self.x += 1

    def haut(self):
        if self.y > 0:
            self.y -= 1

    def bas(self):
        if self.y < self.plateau_size[1] - 1:
            self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation
plateau_size = (5, 5)  
personnage = Personnage(plateau_size=plateau_size)


print("Position initiale du personnage:", personnage.position())


personnage.droite()
personnage.bas()


print("Nouvelle position du personnage:", personnage.position())