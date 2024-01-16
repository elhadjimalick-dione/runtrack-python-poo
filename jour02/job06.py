class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "En cours"

    
    def ajouter_plat(self, nom_plat, prix):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix, "statut": "En cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print(f"Le plat '{nom_plat}' est déjà dans la commande.")

    
    def annuler_commande(self):
        self.__statut_commande = "Annulée"
        print("La commande a été annulée.")

    
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values() if plat["statut"] == "En cours")
        return total

    
    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Commande n°{self.__numero_commande}:")
        for plat, details in self.__plats_commandes.items():
            print(f"- {plat}: {details['prix']} € ({details['statut']})")
        print(f"Total à payer: {total} €")

    
    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * taux_tva / 100
        print(f"Montant de TVA ({taux_tva}%): {tva} €")

# Exemple d'utilisation de la classe Commande
commande_1 = Commande(numero_commande=1)

commande_1.ajouter_plat("riz au poisson", prix=10)
commande_1.ajouter_plat("Yassa poulet", prix=12)

commande_1.afficher_commande()
commande_1.calculer_tva(taux_tva=10)

commande_1.annuler_commande()
commande_1.afficher_commande()