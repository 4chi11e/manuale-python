# 3.29	Creare una matrice che contiene le tabelline dei numeri dall' 1 al 10. Alla fine stamparla.

# metodo classico
tabelline = []
for i in range(10):
    tabelline.append([])
    for j in range(10):
        tabelline[i].append((i+1)*(j+1))

# list comprehension
tabelline = [[(i+1)*(j+1) for j in range(10)] for i in range(10)]

for riga in tabelline:
    for num in riga:
        print(f"{num:3d}", end=" ")
    print("")