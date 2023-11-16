# 45.	Carica un array di numeri casuali, chiedi poi all’utente un numero 
# e digli se questo numero è presente nell’array.

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
    
