for nombre in range(0, 1001):
    est_premier = True
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            est_premier = False
            break
    if est_premier:
        print(nombre)