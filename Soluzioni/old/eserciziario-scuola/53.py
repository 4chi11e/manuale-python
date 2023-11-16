# 53.	Scrivi un programma che istanzia una matrice n x m di interi casuali
# (n e m scelti da te). Oltre a stampare l'intera matrice, chiedi all'utente
# quale riga o quale colonna stampare e stampala sullo schermo
import random
import os
os.system('cls')


# lettura delle dimensioni della matrice
n = int(input("Scrivi il numero di righe (min 1 max 20): "))
while n<1 or n>20:
    n = int(input("Input errato, inserisci un numero tra 1 e 20: "))

m = int(input("Scrivi il numero di colonne: "))
while m<1 or m>20:
    m = int(input("Input errato, inserisci un numero tra 1 e 20: "))

# creazione della matrice e inserimento dei numeri casuali
# matrice = []
# for i in range(n):
#     riga = []
#     for j in range(m):
#         riga.append(random.randint(1, 99))
#     matrice.append(riga)

matrice = [[random.randint(1, 99) for i in range(m)] for j in range(n)]


# stampa della matrice
for riga in matrice:
    for numero in riga:
        print(f"{numero:3d}", end=" ")
    print("")

scelta_riga_colonna = int(input(
    "Scegli se stampare una riga o una colonna (scrivi 0 per riga, 1 per colonna) "))
while scelta_riga_colonna != 1 and scelta_riga_colonna != 0:
    scelta_riga_colonna = int(input("Input errato, reinserisci: "))

if scelta_riga_colonna == 0:
    numero_riga_colonna = int(input(f"Scegli la riga da stampare (le righe vanno da 0 a {n-1}): "))
    while numero_riga_colonna < 0 or numero_riga_colonna >= n:
        numero_riga_colonna = int(input("Input errato, reinserisci: "))
    for numero in matrice[numero_riga_colonna]:
        print(numero, end=" ")
    
else:
    numero_riga_colonna = int(input(f"Scegli la colonna da stampare (le righe vanno da 0 a {m-1}): "))
    while numero_riga_colonna < 0 or numero_riga_colonna >= m:
        numero_riga_colonna = int(input("Input errato, reinserisci: "))
    for riga in matrice:
        print(riga[numero_riga_colonna])


print("\n\n")


def stampa_matrice(M, n, m):
    for riga in M:
        for numero in riga:
            print(numero, end=" ")
            if numero<100:
                print("", end=" ")
            if numero<10:
                print("", end=" ")
        print("")