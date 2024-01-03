class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x) : {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y) : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y


point_instance = Point(3, 5)


point_instance.afficherLesPoints()


point_instance.afficherX()
point_instance.afficherY()

point_instance.changerX(7)
point_instance.changerY(10)


point_instance.afficherLesPoints()