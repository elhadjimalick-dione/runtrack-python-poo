class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero_compte} - Titulaire: {self.__prenom} {self.__nom}")
        print(f"Solde: {self.__solde} €")
        print(f"Découvert autorisé: {'Oui' if self.__decouvert else 'Non'}")

    def afficher_solde(self):
        print(f"Solde actuel: {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")
        else:
            print("Opération impossible. Solde insuffisant.")

    def agios(self, taux):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux
            self.__solde -= agios
            print(f"Agios de {agios} € appliqués. Nouveau solde: {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Opération impossible. Solde insuffisant.")

compte1 = CompteBancaire(numero_compte="123456", nom="Dione", prenom="Malick", solde=1000)


compte1.afficher()
compte1.versement(500)
compte1.retrait(200)
compte1.agios(taux=0.05)
compte1.afficher_solde()


compte2 = CompteBancaire(numero_compte="654321", nom="Diop", prenom="Fadel", solde=-500, decouvert=True)


compte1.virement(compte2, 300)
compte1.afficher()
compte2.afficher()