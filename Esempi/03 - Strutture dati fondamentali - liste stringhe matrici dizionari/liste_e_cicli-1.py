import os
os.system("cls")

lista = ["Sampdoria", "Atalanta", "Hellas", "Lazio", "Inter", "Juventus"]


print("FOR nello stile C , con un indice che percorre gli elementi:")
for i in range(len(lista)):
    print(lista[i])


print("\nFOR come foreach:")
for item in lista:
    print(item)


print("\nWhile:")
i = 0 
while(i < len(lista)):             # uguale al C
    print(lista[i])
    i += 1


# per ottenere sia gli elementi che gli indici (molto comodo!)
print("\nEnumerate:")
for i, el in enumerate(lista):
    print(f"{i:2d}: {el}")
