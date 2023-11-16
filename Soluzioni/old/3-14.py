# 3.14	Dato un array di numeri interi casuali, stampa tutti i numeri superiori alla media partendo dal fondo

import random

A = [random.randint(0, 99) for _ in range(20)]
print(A)

media = sum(A) / len(A)

print(media)

# for num in reversed(A):
for num in A[::-1]:
    if num > media:
        print(num, end=" ")
