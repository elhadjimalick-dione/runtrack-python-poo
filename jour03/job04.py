class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts_marques += 1
        print(f"{self.nom} a marqué un but!")

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a réalisé une passe décisive!")

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune.")

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge!")

    def afficher_statistiques(self):
        print(f"\nStatistiques de {self.nom} (Numéro {self.numero}, Position {self.position}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)
        print(f"{joueur.nom} a été ajouté à l'équipe {self.nom}.")

    def afficher_statistiques_joueurs(self):
        print(f"\nStatistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueur(self, numero_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.numero == numero_joueur:
                if action == "but":
                    joueur.marquer_un_but()
                elif action == "passe":
                    joueur.effectuer_une_passe_decisive()
                elif action == "jaune":
                    joueur.recevoir_un_carton_jaune()
                elif action == "rouge":
                    joueur.recevoir_un_carton_rouge()
                else:
                    print("Action non reconnue.")


joueur1 = Joueur("Aubameyang", 10, "Attaquant")
joueur2 = Joueur("Mbappé", 7, "Attaquant")
joueur3 = Joueur("Ndiaye", 29, "Milieu")
joueur4 = Joueur("Kimpembe", 3, "Défenseur")


equipe1 = Equipe("Marseille")
equipe2 = Equipe("Paris")

equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur3)
equipe2.ajouter_joueur(joueur2)
equipe2.ajouter_joueur(joueur4)


equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()

equipe1.mettre_a_jour_statistiques_joueur(10, "but")
equipe1.mettre_a_jour_statistiques_joueur(11, "passe")
equipe2.mettre_a_jour_statistiques_joueur(7, "jaune")
equipe2.mettre_a_jour_statistiques_joueur(3, "rouge")

# Affichage des statistiques mises à jour des joueurs après le match
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()