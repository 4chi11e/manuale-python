# 3.2.8	Leggi una stringa da input e poi modificala in modo da ottenere la stringa inversa (ad esempio “ciao” diventa “oaic”). Stampa infine la stringa.

import os
os.system('cls')

stringa = input("Scrivi qualcosa: ")
print(stringa)
stringa = stringa[::-1]
print(stringa)
print("\n\n")
