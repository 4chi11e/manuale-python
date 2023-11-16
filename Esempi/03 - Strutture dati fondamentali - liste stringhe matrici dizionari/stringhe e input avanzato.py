# se voglio leggere da input (o poi da file è analogo) più valori devo usare split

s = input("Scrivi dei numeri: ")        # normale input
numeri = list(map(int, s.split()))      # split divide la stringa s in una lista di parole poi map trasforma ogni parola in int, poi lo riconverto in lista perchè se no ho uno strano oggetto map object
print(numeri)