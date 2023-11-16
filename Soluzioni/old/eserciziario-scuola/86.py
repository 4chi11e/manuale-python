# 86.	Scrivi un programma che sappia riordinare un array. Per farlo dividi le seguenti funzionalità
# in diverse funzioni:
# •	funzione che scambia il valore di due variabili
# •	funzione che riceve un array e lo riempie di numeri casuali
# •	funzione che stampa un array
# •	funzione che riceve un array e lo ordina. Lo scambio del valore delle variabili deve essere fatto
#   usando la funzione descritta sopra
# •	main che dichiara un array e poi usando le funzioni descritte sopra lo riempie di numeri casuali,
#   lo stampa, lo ordina e poi lo ristampa.

import random


def stampa_lista(lista):
    for elemento in lista:
        print(elemento, end=" ")
    print()


def ordina(lista):
    if(type(lista) == list):
        # lista.sort()
        
        for i in range(len(lista)):
            for j in range(len(lista)-1):
                if(lista[j] > lista[j+1]):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        # print("\nlista ordinata")


lista = [random.randrange(10) for i in range(5)]
stampa_lista(lista)
ordina(lista)
stampa_lista(lista)
