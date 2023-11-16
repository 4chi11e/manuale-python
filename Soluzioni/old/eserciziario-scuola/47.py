# 47.	Leggi una stringa da input e poi stampala in due modi diversi, 
# la prima volta tutta insieme poi stampando una lettera per volta 
# separando le lettere con uno spazio.

import os
os.system('cls')

stringa = input("Scrivi qualcosa: ")
print(stringa)
for lettera in stringa:
    print(lettera, end=" ")
print("\n\n")