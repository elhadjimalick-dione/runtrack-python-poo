class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Prix HT : {self.prixHT} euros")
        print(f"TVA : {self.TVA}%")
        print(f"Prix TTC : {self.calculerPrixTTC()} euros")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA


produit1 = Produit("Produit1", 50, 20)
produit2 = Produit("Produit2", 30, 10)
produit3 = Produit("Produit3", 80, 15)


produit1.afficher()
produit2.afficher()
produit3.afficher()


produit1.modifierNom("NouveauProduit1")
produit1.modifierPrixHT(60)

produit2.modifierNom("NouveauProduit2")
produit2.modifierPrixHT(40)

produit3.modifierNom("NouveauProduit3")
produit3.modifierPrixHT(90)


print("\nInformations après modification :")
produit1.afficher()
produit2.afficher()
produit3.afficher()