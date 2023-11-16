import os
os.system("cls")

lista = []
for i in range(1,11):
    lista.append(i)
# che equivale a:
lista = [i for i in range(1,11)]
print("\nlista = [i for i in range(1,11) if i%2==0]\n", lista)


l1 = [i for i in range(1,11) if i%2==0]
print("\nlista = [i for i in range(1,11) if i%2==0]\n", l1) 


import random
numeri = [random.randint(0,9) for _ in range(10)]
print("\nnumeri = [random.randint(0,9) for _ in range(10)]\n", numeri)


numeri = [random.random()*10 for i in range(10)]
print("\nnumeri = [random.random()*10 for i in range(10)]\n", numeri)


valori = [0 for i in range(10)]
print("\nvalori = [0 for i in range(10)]\n", valori)


# matrice 4x3 di soli 0
mat = [[0 for j in range(3)] for i in range(4)]
print("\nmat = [[0 for j in range(3)] for i in range(4)]\n", mat)


# tabelline
tabelline = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(tabelline)
print("\n\nStampo le tabelline:")
for riga in tabelline:
    for num in riga:
        print(f"{num:3d}", end=" ")
    print()