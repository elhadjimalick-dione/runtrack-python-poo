class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def ajouter_population(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouter_population(self):
        self.__ville.ajouter_population()


paris = Ville("Paris", 1000000)


print(f"Population de la ville de Paris : {paris.get_nombre_habitants()} habitants")

marseille = Ville("Marseille", 861635)

print(f"Population de la ville de Marseille : {marseille.get_nombre_habitants()} habitants")


john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)


paris.ajouter_population()
paris.ajouter_population()
marseille.ajouter_population()

print(f"Mise a jour de la population de la ville de Paris : {paris.get_nombre_habitants()} habitants")
print(f"Mise a jour de la population de la ville de Marseille  : {marseille.get_nombre_habitants()} habitants")