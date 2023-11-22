def simulation_financiere(montant_initial, taux_rendement_annuel, annees):
    for annee in range(1, annees + 1):
        gain_annuel = montant_initial * taux_rendement_annuel / 100
        montant_initial += 5000
        montant_initial += gain_annuel
        taux_rendement_annuel += 2 
        
        print(f"Année {annee}: Gain annuel = {gain_annuel:.2f} euros, Montant après rendement = {montant_initial:.2f} euros")

        nouveau_gain = montant_initial * taux_rendement_annuel / 100
        print(f"Année {annee}: Calcul du gain après l'augmentation du capital de 5000 euros et du taux de rendement de 2% = {nouveau_gain:.2f} euros")

    retrait = montant_initial * 0.10
    montant_initial -= retrait

    taux_rendement_annuel -= 1

    nouveau_gain_final = montant_initial * taux_rendement_annuel / 100

    print(f"\nMontant final après retrait de 10% et diminution du rendement de 1% = {montant_initial:.2f} euros")
    print(f"Nouveau gain final = {nouveau_gain_final:.2f} euros")

montant_initial = float(input("Entrez le montant initial de l'investissement en euros : "))
taux_rendement_annuel = float(input("Entrez le taux de rendement annuel en pourcentage : "))
annees = int(input("Entrez le nombre d'années pour la simulation : "))

simulation_financiere(montant_initial, taux_rendement_annuel, annees)