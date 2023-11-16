# 43.	Leggi n voti, caricali in un array, calcolane la media, poi stampa tutti i numeri e la media.

numeri = []
n = int(input("Dimmi quanti numeri vuoi inserire:"))
media = 0
for i in range(n):
    numero = int(input(f"Scrivi il {i+1}° numero: "))
    while numero < 1 or numero > 10:
        numero = int(input("\nVoto non valido, reinseriscilo: "))
    numeri.append(numero)
    media += numero
media /= n
print("\nI numeri inseriti sono:")
for numero in numeri:
    print(numero, end=" ")
# print("\nLa media dei numeri è", round(media, 2))
print(f"\nLa media dei numeri è {media:.2f}")
