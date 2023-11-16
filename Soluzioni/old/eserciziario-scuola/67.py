# 67.	Scrivi un programma che dato un array di numeri interi, sia in grado di:
# •	controllare se l'array è palindromo,
# •	invertire l'ordine dei numeri dell'array,
# •	ordinare in ordine decrescente l'array.

numeri = [10,13,6,13,7]

# controllare se l'array è palindromo
if numeri == numeri[::-1]:
    print(f"{numeri} è palindromo")
else:
    print(f"{numeri} non è palindromo")

# invertire l'ordine dei numeri dell'array,
numeri = numeri[::-1]
print(numeri)

# ordinare in ordine decrescente l'array.
numeri.sort(reverse=True)
print(numeri)

