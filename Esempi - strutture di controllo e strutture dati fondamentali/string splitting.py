s = "Ciao a tutti, come vi sentite oggi? Io bene, grazie!"

lista = s.split()
print(lista)

lista = s.split(",") # puoi indicare un separatore
print(lista)

# se si desidera usare più separatori sono necessarie tecniche più elaborate
# 1. split più di una volta
lista = []
tmp = s.split(",")
for el in tmp:
    el = el.split("?")
    lista += el
print(lista)

# 2. usare le espressioni regolari
import re
lista = re.split(r",|\?|!", s) # r indica che la stringa è in realtà una espressione regolare, \? perchè ? è un carattere speciale

# se voglio togliere le stringhe vuote
lista = list(filter(None, lista)) 
# si può fare tutto in un solo comando
lista = list(filter(None, re.split(r",|\?|!| ", s))) 

print(lista)

