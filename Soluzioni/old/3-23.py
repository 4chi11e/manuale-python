# 3.23	Leggi usando un’unica funzione input tre parole. Indica poi qual è la parola più lunga, la parola che viene prima in ordine alfabetico e la parola che contiene più vocali.

def conta_vocali(s):
    ris = 0
    for l in s:
        if l in "aeiou":
            ris += 1
    return ris

parole = input("Scrivi tre parole:")
parole = parole.split()
parole = list(map(str.strip, parole))

print(parole)

parole.sort(key=lambda el: len(el))
print("La parola più lunga:", parole[-1])

parole.sort(key=lambda el: str.lower(el))
print("La parola che viene prima in ordine alfabetico:", parole[0])

parole.sort(key=conta_vocali)
print("La parola che contiene più vocali:", parole[-1])