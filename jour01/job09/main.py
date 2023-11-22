class Produit:
    def __init__(self, nom, prix_unitaire, quantite_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_stock = quantite_stock

    def afficher_informations(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Prix unitaire : {self.prix_unitaire} euros")
        print(f"Quantité en stock : {self.quantite_stock} unités")

    def ajouter_stock(self, quantite_ajoutee):
        self.quantite_stock += quantite_ajoutee
        print(f"{quantite_ajoutee} unité(s) ajoutée(s) en stock. Nouvelle quantité en stock : {self.quantite_stock} unités")

    def mise_a_jour_prix(self, pourcentage_augmentation):
        self.prix_unitaire *= (1 + pourcentage_augmentation / 100)
        print(f"Le prix du produit a augmenté de {pourcentage_augmentation}%. Nouveau prix unitaire : {self.prix_unitaire} euros")

    def mise_a_jour_prix(self, pourcentage_augmentation):
        self.prix_unitaire *= (1 + pourcentage_augmentation / 100)
        print(f"Le prix du produit a augmenté de {pourcentage_augmentation}%. Nouveau prix unitaire : {self.prix_unitaire} euros")
        return self


nom_produit = input("Entrez le nom du produit : ")
prix_unitaire_produit = float(input("Entrez le prix unitaire du produit en euros : "))
quantite_stock_produit = int(input("Entrez la quantité de produits à ajouter en stock : "))

produit = Produit(nom_produit, prix_unitaire_produit, quantite_stock_produit)

produit.afficher_informations()

quantite_ajoutee = int(input("Entrez la quantité de produits à ajouter en stock : "))
produit.ajouter_stock(quantite_ajoutee)

pourcentage_augmentation = 10
produit.mise_a_jour_prix(pourcentage_augmentation)

print("\nInformations après la mise à jour du prix et ajout en stock :")
produit.afficher_informations()