class Student:
    def __init__(self, first_name, last_name, student_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print("Nom = {}".format(self.__last_name))
        print("Prénom = {}".format(self.__first_name))
        print("Id = {}".format(self.__student_id))
        print("Niveau = {}".format(self.__level))

    def get_nom(self):
        return self.__last_name

    def get_prenom(self):
        return self.__first_name

    def get_credits(self):
        return self.__credits


john_doe = Student("John", "Doe", 145)


john_doe.add_credits(15)
john_doe.add_credits(5)
john_doe.add_credits(10)


john_doe.student_info()

# Impression du total de crédits de l'étudiant
print(f"Le nombre de crédits de {john_doe.get_nom()} {john_doe.get_prenom()} est de: {john_doe.get_credits()} points")