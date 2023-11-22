def contient_e(chaine):
    if 'e' in chaine:
        return True
    else:
        return False

chaine_test = input("Entrez une chaîne de caractères : ")
resultat = contient_e(chaine_test)

if resultat:
    print("La chaîne contient le caractère 'e'.")
else:
    print("La chaîne ne contient pas le caractère 'e'.")