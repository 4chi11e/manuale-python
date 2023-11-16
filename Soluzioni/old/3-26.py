# 3.26	Scrivi due funzioni che implementino il cifrario di Cesare cioè un cifrario che per cifrare un testo trasforma ogni lettera nella lettera che si trova tre posizioni più avanti nell’alfabeto. Le due funzioni sono le funzioni “cifra” e “decifra”. Scrivi infine u programma che permetta di inserire un testo da cifrare o decifrare a scelta.

import string

minuscole = string.ascii_lowercase
maiuscole = string.ascii_uppercase

def cifra(testo, chiave):
    cifrato = ""
    for i in range(len(testo)):
        if testo[i] in minuscole:
            offset = ord('a')
        elif testo[i] in maiuscole:
            offset = ord('A')
        else:
            offset = 0
        if offset != 0:
            cifrato += chr(((ord(testo[i]) - offset + chiave) % len(minuscole)) + offset)
        else:
            cifrato += testo[i]
    return cifrato

def decifra(testo, chiave):
    decifrato = ""
    for i in range(len(testo)):
        if testo[i] in minuscole:
            offset = ord('a')
        elif testo[i] in maiuscole:
            offset = ord('A')
        else:
            offset = 0
        if offset != 0:
            decifrato += chr(((ord(testo[i]) - offset - chiave) % len(minuscole)) + offset)
        else:
            decifrato += testo[i]
    return decifrato

testo = input("Inserisci un testo: ")
chiave = int(input("Inserisci la chiave: "))
scelta = int(input("Vuoi cifrare o decifrare? scrivi 1 per cifrare, 2 per decifrare: "))
while scelta != 1 and scelta != 2:
    scelta = input("Risposta non prevista, scrivi 1 per cifrare, 2 per decifrare: ")
if scelta == 1:
    testo = cifra(testo, chiave)
    print("Il messaggio cifrato è:")
    print(testo)
else:
    testo = decifra(testo, chiave)
    print("Il messaggio decifrato è:")
    print(testo)





