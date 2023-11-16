# 1.	Data l’area del cerchio, stampare la circonferenza

import math

area = float(input("inserisci l'area del cerchio: "))
circonferenza = 2*math.pi*(area/math.pi)**(1/2)
print("circonferenza: ", circonferenza)


# 2.	Data la base e l’altezza di un triangolo, scrivere l’area

base = float(input("scrivi il valore della base: "))
altezza = float(input("scrivi il valore dell'altezza': "))
area = base*altezza/2
print("L'area è: ", area)


# 4.	Dati due numeri calcolare il loro quoziente se il divisore è <> 0, ritornare “impossibile” se il divisore = 0

num = float(input("scrivi il valore del numeratore: "))
den = float(input("scrivi il valore del denominatore': "))
if den == 0:
    print("Non è possibile dividere per 0")
else:
    print(num, "/", den, " = ", num/den)


# 5.	Divisione di due numeri senza usare l’operatore di divisione

num = int(input("scrivi il valore del numeratore: "))
den = int(input("scrivi il valore del denominatore': "))

ris = 0
resto = num
while resto > den:
    resto -= den
    ris += 1
print(num, "/", den, " = ", ris, " resto ", resto)


# 7.	Inserire n numeri != 0 (0 per finire), contare quanti sono i numeri inseriti

# VERSIONE 1
c = 0
num = -1
while num!=0:
  num=int(input("scrivi un numero, 0 per uscire: "))
  if num!=0:
    c+=1
print(c)

# VERSIONE 2
c = 0
num = -1
while True:
  num=int(input("scrivi un numero, 0 per uscire: "))
  if num == 0:
    break
  c+=1
print(c)


# 8.	Moltiplicazione di due numeri senza usare l’operatore di moltiplicazione

a = int(input("scrivi il primo valore: "))
b = int(input("scrivi il secondo valore: "))

ris=0
for i in range(b):
  ris += a
print(a, " x ", b, " = ", ris)


# 9.	Dati tre numeri reali dire che tipo di triangolo essi formano (classificazione dei triangoli in base ai lati).

a = float(input("scrivi il primo valore: "))
b = float(input("scrivi il secondo valore: "))
c = float(input("scrivi il terzo valore: "))

if a==b and b==c:
  ris = "equilatero"
elif a==b or b==c or a==c:
  ris = "isoscele"
else:
  ris = "scaleno"

print(a, ", ", b, ", ", c, " formano un triangolo ", ris)


# 10.	Data una sequenza di n numeri interi, calcolare la somma dei pari ed il prodotto dei dispari 

# VERSIONE 1
n = int(input("Scrivi quanti numeri vuoi inserire: "))
somma = 0
prodotto = 1

for i in range(n):
  num = float(input("Scrivi il "+str(i+1)+"° numero: "))
  if num%2 == 0: #cioè se è pari
    somma+=num
  else:
    prodotto*=num

print("somma dei pari: ", somma)
print("prodotto dei dispari: ", prodotto)


# VERSIONE 2
n = int(input("Scrivi quanti numeri vuoi inserire: "))
somma = 0
prodotto = 1

l = []

for i in range(n):
  num = int(input("Scrivi il "+str(i+1)+"° numero: "))
  l.append(num)

print(l)

for num in l:
  if num%2 == 0: #cioè se è pari
    somma+=num
  else:
    prodotto*=num

print("somma dei pari: ", somma)
print("prodotto dei dispari: ", prodotto)




# 43.	Leggi n voti, caricali in un array, calcolane la media, poi stampa tutti i numeri e la media.

numeri = []
n = int(input("Dimmi quanti numeri vuoi inserire:"))
media = 0
for i in range(n):
    numero = int(input(f"Scrivi il {i+1}° numero: "))
    while numero < 1 or numero > 10:
        numero = int(input("\nVoto non valido, reinseriscilo: "))
    numeri.append(numero)
    media += numero
media /= n
print("\nI numeri inseriti sono:")
for numero in numeri:
    print(numero, end=" ")
print("\nLa media dei numeri è", round(media, 2))



# 45.	Carica un array di numeri casuali, chiedi poi all’utente un numero e digli se questo numero è presente nell’array.

import random

numeri = []
for i in range(20):
    numeri.append(random.randint(0,99))

print(numeri)

numero = int(input("Dimmi un numero da cercare:"))

if numero in numeri:
    print("il numero è presente nella lista")
else:
    print("il numero non è presente nella lista")



# 46.	Leggi una stringa da input e poi comunica all’utente di quante lettere è composta la stringa. Il conteggio deve essere fatto in due modi diversi, usando la funzione strlen e contando i caratteri uno alla volta.

stringa = input("Scrivi qualcosa: ")

# print(stringa)

numero_lettere = 0
for lettera in stringa:
    numero_lettere += 1

print(f"Contando i caratteri uno alla volta ho contato {numero_lettere} lettere")

numero_lettere = len(stringa)
print(f"\nContando i caratteri con la funzione len ho contato {numero_lettere} lettere")




# 47.	Leggi una stringa da input e poi stampala in due modi diversi, la prima volta tutta insieme poi stampando una lettera per volta separando le lettere con uno spazio.

stringa = input("Scrivi qualcosa: ")
print(stringa)
for lettera in stringa:
    print(lettera, end=" ")



# 48.	Leggi una stringa da input e poi stampala al contrario, cioè partendo dal fondo ma non modificandone il contenuto.

stringa = input("Scrivi qualcosa: ")
print(stringa)
for lettera in reversed(stringa):
    print(lettera, end="")



# 49.	Leggi una stringa da input e poi modificala in modo da ottenere la stringa inversa (ad esempio “ciao” diventa “oaic”). Stampa infine la stringa.

stringa = input("Scrivi qualcosa: ")
print(stringa)
stringa = stringa[::-1]
print(stringa)





# 51.	Leggi da input due stringhe, se le due stringhe sono uguali comunica che sono uguali altrimenti scrivi quella che viene prima in ordine alfabetico

stringa1 = input("Scrivi la prima stringa: ")
stringa2 = input("Scrivi la seconda stringa: ")

if stringa1 == stringa2:
    print("Le stringhe sono uguali\n\n")
else:
    prima = (stringa1, stringa2)[stringa1 > stringa2]
    print(f"La stringa che viene prima in ordine alfabetico è: {prima}\n\n")





# MATRICI
# 52.	Creare una matrice che contiene le tabelline dei numeri dall' 1 al 10. Alla fine stamparla.

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




# 53.	Scrivi un programma che istanzia una matrice 	n x m di interi casuali (n e m scelti da te). Oltre a stampare l'intera matrice, chiedi all'utente quale riga o quale colonna stampare e stampala sullo schermo

# lettura delle dimensioni della matrice
n = int(input("Scrivi il numero di righe: "))
m = int(input("Scrivi il numero di colonne: "))

# creazione della matrice e inserimento dei numeri casuali
matrice = []
for i in range(n):
    riga = []
    for j in range(m):
        riga.append(random.randint(1, 99))
    matrice.append(riga)

# stampa della matrice
for riga in matrice:
    print(riga)

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





# 54.	Scrivere un programma che riempia due matrici A e B di dimensione n x m e calcoli la matrice C = A + B e la matrice D = A x B (in realtà è un finto prodotto di matrici). Stampa le matrici ottenute. Per il calcolo della somma calcola normalmente C[i][j] = A[i][j] + B[i][j] mentre per la moltiplicazione hai due possibilità:
# •	Versione semplice se non riesci proprio a fare la versione corretta: C[i][j] = A[i][j] x B[i][j].
# •	Versione complicata: vai a guardare su internet come si calcola e scrivi l’algoritmo per farlo.

def stampa_matrice(M, n, m):
    for riga in M:
        for numero in riga:
            print(numero, end=" ")
            if numero<100:
                print("", end=" ")
            if numero<10:
                print("", end=" ")
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
stampa_matrice(A,n,m)
print("\nMatrice B:")
stampa_matrice(B,n,m)
# print(f"A: {A}")
# print(f"B: {B}")

# creazione e calcolo di C
C = []
for i in range(n):
    riga = []
    for j in range(m):
        riga.append(A[i][j] + B[i][j])
    C.append(riga)
# print(f"C: {C}")
print("\nMatrice C:")
stampa_matrice(C,n,m)

# creazione e calcolo di D (semplice)
D = []
for i in range(n):
    riga = []
    for j in range(m):
        riga.append(A[i][j] * B[i][j])
    D.append(riga)
# print(f"D semplice: {D}")
print("\nMatrice D semplice:")
stampa_matrice(D,n,m)

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
    print("\nMatrice D normale:")
    stampa_matrice(D,n,m)


