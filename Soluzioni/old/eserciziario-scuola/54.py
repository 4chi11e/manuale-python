# 54.	Scrivere un programma che riempia due matrici A e B
# di dimensione n x m e calcoli la matrice C = A + B e
# la matrice D = A x B (in realtà è un finto prodotto di matrici).
# Stampa le matrici ottenute. Per il calcolo della somma calcola
# normalmente C[i][j] = A[i][j] + B[i][j] mentre per la moltiplicazione
# hai due possibilità:
# •	Versione semplice se non riesci proprio a fare la versione corretta: C[i][j] = A[i][j] x B[i][j].
# •	Versione complicata: vai a guardare su internet come si calcola e scrivi l’algoritmo per farlo.


import random
import os
os.system('cls')

def stampa_matrice(M):
    for riga in M:
        for numero in riga:
            print(f"{numero:3d}", end=" ")
        print("")


# creazione e riempimento di A e B
n = 2
m = 2
A = []
B = []
for i in range(n):
    rigaA = []
    rigaB = []
    for j in range(m):
        rigaA.append(random.randint(1, 9))
        rigaB.append(random.randint(1, 9))
    A.append(rigaA)
    B.append(rigaB)

print("Matrice A:")
stampa_matrice(A)
print("\nMatrice B:")
stampa_matrice(B)

# creazione e calcolo di C
C = []
for i in range(n):
    riga = []
    for j in range(m):
        riga.append(A[i][j] + B[i][j])
    C.append(riga)
# print(f"C: {C}")
print("\nMatrice C:")
stampa_matrice(C)

# creazione e calcolo di D (semplice)
D = []
for i in range(n):
    riga = []
    for j in range(m):
        riga.append(A[i][j] * B[i][j])
    D.append(riga)
# print(f"D semplice: {D}")
print("\nMatrice D semplice:")
stampa_matrice(D)

# calcolo di D normale
if m != n:
    print("Il prodotto tra A e B non si può calcolare")
else:
    D = []
    for i in range(n):
        riga = []
        for j in range(m):
            somma = 0
            for k in range(m):
                somma += A[i][k] * B[k][j]
            riga.append(somma)
        D.append(riga)
    # non sono sicuro del risultato
    # print(f"D completo: {D}")
    print("\nMatrice D normale: (da rivedere il procedimento)")
    stampa_matrice(D)


print("\n\n")
