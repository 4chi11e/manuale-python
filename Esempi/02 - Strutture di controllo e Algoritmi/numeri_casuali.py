import os
os.system("cls")


import random

lista = [random.randint(0, 10) for _ in range(5)]   # genera 5 numeri interi casuali tra 0 e 10 compresi
print(lista)

lista = [random.random() for _ in range(5)]   # genera 5 numeri float tra 0 e 1 ESCLUSO
print(lista)

# posso poi farci quello che voglio
lista = [round(random.random()*100, 2) for _ in range(5)]   # genero 5 percentuali approssimate al secondo decimale
print(lista)
