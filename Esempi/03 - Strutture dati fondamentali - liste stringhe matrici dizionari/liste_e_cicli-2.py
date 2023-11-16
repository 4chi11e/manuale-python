import os
os.system("cls")


lista = [0,1,2,3,4,5,6,7]

print("Normale:")
for el in lista:
    print(el, end=" ")
print("\n")

print("Con passo 2:")
for el in lista[::2]:
    print(el, end=" ")
print("\n")

print("Al contrario 1:")
for el in lista[::-1]:
    print(el, end=" ")
print("\n")

print("Al contrario 2:")
for el in reversed(lista):
    print(el, end=" ")
print("\n")

print("Dritto con indice i:")
for i in range(len(lista)):
    print(lista[i], end=" ")
print("\n")

print("Al contrario con indice i 1:")
for i in reversed(range(len(lista))):
    print(lista[i], end=" ")
print("\n")

print("Al contrario con indice i 2:")
for i in range(len(lista)-1, -1, -1): # dall'ultima posizione alla -1 esclusa (quindi 0) con passo -1
    print(lista[i], end=" ")
print("\n")

print("Dalla posizione 2 alla 4 comprese:")
for el in lista[2:5]:
    print(el, end=" ")
print("\n")

print("Dalla posizione 2 alla 4 comprese al contrario:")
for el in lista[4:1:-1]:
    print(el, end=" ")
print("\n")

print("Dalla posizione 2 alla 4 comprese al contrario con passo 2:")
for el in lista[4:1:-2]:
    print(el, end=" ")
print("\n")


# esempio con enumerate. Attenzione che non prende gli indici della lista originale ma della lista ottenuta
print("Enumerate:")
for i, el in enumerate(lista[::2]):
    print(f"{i:2d}: {el}")





