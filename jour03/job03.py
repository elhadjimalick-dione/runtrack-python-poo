class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée à la liste.")

    def supprimerTache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"Tâche '{tache.titre}' supprimée de la liste.")
        else:
            print("Cette tâche n'est pas dans la liste.")

    def marquerCommeFinie(self, tache):
        if tache in self.taches:
            tache.statut = "Terminée"
            print(f"Tâche '{tache.titre}' marquée comme terminée.")
        else:
            print("Cette tâche n'est pas dans la liste.")

    def afficherListe(self):
        print("Liste des tâches :")
        for tache in self.taches:
            print(f"Titre: {tache.titre}, Description: {tache.description}, Statut: {tache.statut}")

    def filterListe(self, statut):
        taches_filtrées = [tache for tache in self.taches if tache.statut == statut]
        return taches_filtrées

# Tester le code
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Répondre aux e-mails", "Répondre aux e-mails professionnels")
tache3 = Tache("Faire du sport", "30 minutes de jogging")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

liste_taches.afficherListe()

liste_taches.supprimerTache(tache2)

liste_taches.marquerCommeFinie(tache1)

taches_a_faire = liste_taches.filterListe("À faire")

print("\nTâches à faire :")
for tache in taches_a_faire:
    print(f"Titre: {tache.titre}, Description: {tache.description}, Statut: {tache.statut}")