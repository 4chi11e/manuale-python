# 68.	Dato un array di stringhe (quindi una matrice di caratteri), 
# che puoi riempire come preferisci, ordina l’array in ordine alfabetico 
# prima crescente e poi decrescente. Devono essere inserite le stampe 
# dell’intero array prima e dopo ogni ordinamento.

elenco = ["ciao belli", "come state?", "Io bene"]
print(elenco)

elenco.sort()
print(elenco)

elenco.sort(reverse=True)
print(elenco)

