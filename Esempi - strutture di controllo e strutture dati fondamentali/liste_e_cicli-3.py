import os
os.system("cls")


lista = [0,1,2,3,4,5,6,7]


print("> print(lista)\n" ,lista)

print("\n> print(lista[::2])\n" ,lista[::2])

print("\n> print(lista[::-1])\n" ,lista[::-1])

print("\n> print(reversed(lista))\n" ,reversed(lista)) # attento il reversed lo puoi usare solo come generatore nei cicli for (come il range())


# esiste una funzione reverse delle liste che ti modifica la lista stessa e non restituisce nulla
inversa = lista
inversa.reverse()
print("\n> inversa = lista\n> inversa.reverse()\n> print(inversa)\n", inversa)

print("\n> print(lista[::2])\n" ,lista[::2])
print("\n> print(lista[::2])\n" ,lista[::2])
print("\n> print(lista[::2])\n" ,lista[::2])


print("\n> print(lista[2:5])\n" ,lista[2:5])

print("\n> print(lista[4:1:-1])\n" ,lista[4:1:-1])

print("\n> print(lista[4:1:-2])\n" ,lista[4:1:-2])






