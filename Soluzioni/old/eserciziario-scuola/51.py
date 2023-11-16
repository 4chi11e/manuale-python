# 51.	Leggi da input due stringhe, se le due stringhe sono uguali 
# comunica che sono uguali altrimenti scrivi quella che viene prima in ordine alfabetico

import os
os.system('cls')

stringa1 = input("Scrivi la prima stringa: ")
stringa2 = input("Scrivi la seconda stringa: ")

if stringa1 == stringa2:
    print("Le stringhe sono uguali\n\n")
else:
    prima = (stringa1, stringa2)[stringa1 > stringa2]
    print(f"La stringa che viene prima in ordine alfabetico è: {prima}\n\n")
print("\n\n")
