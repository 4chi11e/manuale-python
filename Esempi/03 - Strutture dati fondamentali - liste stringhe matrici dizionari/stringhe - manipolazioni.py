import os
os.system("cls")


frase = "Ciao a tutti, come state?"


# modifiche all'intera stringa con funzioni
print("\nUpper, capitalize, lower:")
print(frase.upper())
print(frase.capitalize())
print(frase.lower())


# data una stringa, trasforma la stringa in modo tale che
# le lettere in posizione pari siano maiuscole e le altre 
# minuscole

print("\n\n\n - Pari maiuscole, dispari minuscole:\n")

# le funzioni viste sopra funzionano per stringhe non per caratteri singoli, 
# quindi devo trasformare la stringa in una lista e lavorare con i singoli 
# elementi che per me sono singoli caratteri ma in realtà sono stringhe di lunghezza 1

# metodo 1

lista = list(frase)

for i in range(1,len(lista),2):
    lista[i] = lista[i].lower()

for i in range(0,len(lista),2):
    lista[i] = lista[i].upper()

# poi devo unire tutti gli elementi e ricostruire la frase

# 1.1 metodo farlocco di ricostruzione
modificata = ""
for el in lista:
    modificata += el
print("Metodo 1.1:", modificata)

# 1.2 metodo veloce di ricostruzione (funzione join)
modificata = "".join(lista) # non puoi fare str(lista)
print("Metodo 1.2:", modificata)


# metodo 2 più veloce
mod = ""
for i, lettera in enumerate(frase):
    if i % 2 == 0:
        mod += frase[i].upper()
    else:
        mod += frase[i].lower()

print("Metodo 2  :", mod)
