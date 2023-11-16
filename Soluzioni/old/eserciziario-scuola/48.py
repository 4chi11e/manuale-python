# 48.	Leggi una stringa da input e poi stampala al contrario, 
# cioè partendo dal fondo ma non modificandone il contenuto.

import os
os.system('cls')

stringa = input("Scrivi qualcosa: ")
print(stringa)
for lettera in reversed(stringa):
    print(lettera, end="")
print("\n\n")
