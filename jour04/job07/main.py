L = [8,24,48,2,16]

x3 = 0

for nombre in L:
    if nombre % 3 == 0:
        x3 += 1

print(L)
print(f"Le nombre de multiple de 3 dans la liste est de : {x3}")