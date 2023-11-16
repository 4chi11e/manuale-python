import os
os.system("cls")


frase = "Ciao a tutti, come state?"


# stampa normale
print(" - Stampa normale:")
print(frase)


# stampa carattere per carattere
print("\n - Stampa carattere per carattere:")
for lettera in frase:
    print(lettera, end="")
print()


## stringhe su più righe
print("\n\n\n - Stringhe su più righe:\n")
stringa1 = "Ciao a tutti!"

stringa2 = """
Ciao, come va?
Bene grazie
"""

stringa3 = "Ciao, come va?\nBene grazie"

print(stringa1)
print(stringa2)
print(stringa3)


# char to ascii e viceversa
print("\n\n\n - Char to ASCII e viceversa:\n")

lettera = "A"    # attento che in realtà è una stringa con un solo carattere
print(lettera)

codice = ord(lettera)
print(codice)

lettera = chr(codice)
print(lettera)


# concatenare stringhe
print("\n\n\n - Concatenazione semplice di stringhe:\n")
s1 = "Ciao"
s2 = "belli!"
s3= s1+" "+s2
print(f"'{s1}' + ' ' + '{s2}' = '{s3}'")


# concatenazione con join
# la funzione join in generale unisce tutti gli elementi di una lista 
# aggiungendo come separatore tra ognuno il contenuto della stringa 
# iniziale su cui è chiamato il join
print("\n\n\n - Esempio base join:\n")
frase = ", ".join(["casa", "aereo", "pollo"])
print("frase = \", \".join([\"casa\", \"aereo\", \"pollo\"])")
print(frase)


# eliminare da una stringa spazi o tab iniziali o finali
# strip(): returns a new string after removing any leading and trailing whitespaces including tabs (\t). - comprende le altre due
# rstrip(): returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
# lstrip(): returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.

print("\n\nStrip:\n")

stringa = "   Vediamo come me la CAVO   "  

print("Stringa originale:", stringa)
print("Lunga:", len(stringa))

stringa = stringa.strip()
print("Stringa corretta :", stringa)
print("Lunga:", len(stringa))




