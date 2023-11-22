def type_triangle(a, b, c):

    if a + b > c and a + c > b and b + c > a:

        if a == b == c:
            return "Le triangle est équilatéral."
        elif a == b or a == c or b == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                return "Le triangle est rectangle et isocèle."
            else:
                return "Le triangle est isocèle mais pas rectangle."
        else:
            return "Le triangle est quelconque."
    else:
        return "Les longueurs ne peuvent pas former un triangle."

a = float(input("Entrez la longueur de côté a : "))
b = float(input("Entrez la longueur de côté b : "))
c = float(input("Entrez la longueur de côté c : "))

resultat = type_triangle(a, b, c)
print(resultat)
