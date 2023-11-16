# 52.	Creare una matrice che contiene le tabelline dei numeri dall' 1 al 10. Alla fine stamparla.

import os
os.system('cls')

tabella = []
for i in range(1,11):
    riga = []
    for j in range(1,11):
        riga.append(i*j)
    tabella.append(riga)

for riga in tabella:
    for numero in riga:
        print(numero, end="\t")
    print("")
        
print("\n\n")
