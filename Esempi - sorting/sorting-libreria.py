import random
import os

os.system("cls")

print("Vettore semplice")
V = [random.randint(0, 10) for _ in range(10)]
print(V)
V.sort()
print(V)
V.sort(reverse=True)
print(V)
# print("Se voglio ordinare solo una parte non si può fare nello stesso modo ma posso prenderne solo un pezzo e ordinarlo")
print("\n")



print("Vettore di elementi composti di più cose")
V = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(10)]
print(V)
V.sort()
print(V)
V.sort(reverse=True)
print(V)
print()

print("Se voglio ordinare in base al secondo elemento o in generale gli elementi non sono direttamente ordinabili (ad esempio istanze di mia classe)")
V.sort(key=lambda x: (x[1],x[0])) # ordine crescente in base al secondo elemento e poi in base al primo
print(V)
V.sort(key=lambda x: (-x[1],x[0])) # ordine decrescente in base al secondo elemento e poi in ordine crescente in base al primo
print(V)
V.sort(key=lambda x: (x[1],x[0]), reverse=True) # equivale al precedente
print(V)
