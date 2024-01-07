class Vehicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèl: {self.model}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix} €")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix, portes=4):
        super().__init__(marque, model, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("Vroom Vroom ! La voiture démarre.")


class Moto(Vehicule):
    def __init__(self, marque, model, annee, prix, roues=2):
        super().__init__(marque, model, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print("Vroum Vroum ! La moto démarre.")


# Instanciation de la classe Voiture
voiture1 = Voiture(marque="Mercedes", model="Classe A", annee=2020, prix=18500)

voiture1.informationsVehicule()

voiture1.demarrer()

# Espacement
print("\n")

# Instanciation de la classe Moto
moto1 = Moto(marque="Yamaha", model="1200 Vmax", annee=1987, prix=4500)

moto1.informationsVehicule()

moto1.demarrer()