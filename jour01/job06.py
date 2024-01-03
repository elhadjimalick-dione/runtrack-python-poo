class Animal:
    def __init__(self):
        self.age = 0 
        self.prenom = ""

    def vieillir(self):
        self.age += 1 

    def nommer(self, nom):
        self.prenom = nom


animal_instance = Animal()

animal_instance.nommer("Luna")
print("L'animal se nomme:", animal_instance.prenom)

print("L'age de l'animal :", animal_instance.age, "ans")

animal_instance.vieillir()

# Affichage de l'âge après avoir fait vieillir l'animal
print("L'age de l'animal ans:", animal_instance.age, "ans")