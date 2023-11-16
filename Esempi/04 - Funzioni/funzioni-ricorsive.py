import os;
os.system('cls')

# una funzione può richiamare se stessa
def countdown_infinito(x):
    print(x)
    countdown_infinito(x-1)

# se uso questa funzione non termino mai, serve un if che verifichi il caso finale

def countdown(x):
    print(x)
    if x > 0:
        countdown(x-1)

print("Countdown:")
countdown(5)


# esempio classico il fattoriale https://it.wikipedia.org/wiki/Fattoriale
def fattoriale(x):
    # caso in cui non è definito (x non appartiene al dominio)
    if type(x) is not int or x < 0:
        return None

    # casi finali
    if x == 0:
        return 1

    # tutti gli altri casi
    return x * fattoriale(x-1)

print("\nFattoriale:")
print(f"5! = {fattoriale(5)}")

    

# una funzione può richiamare se stessa più volte
# esempio classico, ennesimo numero della successione di fibonacci 
# https://it.wikipedia.org/wiki/Successione_di_Fibonacci
def fibonacci(x):
    # caso in cui non è definito
    if type(x) is not int or x < 0:
        return None

    # casi finali
    if x == 0:
        return 1

    # tutti gli altri casi
    return fibonacci(x-1) + fibonacci(x-2)

print("\nFibonacci:")
n = 5
print(f"F({n}) = {fibonacci(n)}")
# con numeri bassi funziona ma se provo con numeri alti...
# n = 35
# print(f"F({n}) = {fibonacci(n)}")
# intorno al 35 il mio computer inizia a metterci tanto tempo
# la funzione richiama se stessa sempre 2 volte quindi con n = 35 per arrivare ad n=0 e arrivare al caso finale
# devo fare circa (in realtà un po meno) 2^35 chiamate. Il tempo di calcolo cresce esponenzialmente,
# raddoppia ogni volta che n aumenta di 1. 
# Questo tipo di funzione ricorsiva NON VA BENE!
# il problema è che la funzione viene chiamata tantissime volte per gli stessi valori di n

# in questi casi ho due soluzioni, o riscrivo l'algoritmo passando da una versione ricorsiva ad una iterativa,
# oppure posso introdurre la memoria. Vedremo più avanti queste soluzioni.

# se la funzione richiama se stessa solo per valori diversi dei parametri non ci sono problemi
# un esempio è la ricerca dicotomica

def ricerca_dicotomica_ordinata(lista_ordinata, numero):
    dim = len(lista_ordinata)
    if dim <= 0:
        return False
    else:
        # print(lista_ordinata)
        mezzo = lista_ordinata[dim//2]
        if numero == mezzo:
            return True
        elif numero < mezzo:
            sx = lista_ordinata[:dim//2]
            return ricerca_dicotomica_ordinata(sx, numero)
        else: # numero > mezzo
            dx = lista_ordinata[dim//2 + 1:]
            return ricerca_dicotomica_ordinata(dx, numero)

n = 20
print("\nRicerca dicotomica lista ordinata, cerco", n)
from random import randint
lista = [randint(0,50) for _ in range(20)]
lista.sort()
# print(lista)
print(ricerca_dicotomica_ordinata(lista, 20))

# in questo caso il tempo di ricerca è log_2(n) perchè ad ogni chiamata la dimensione della lista
# che considero si dimezza (contrario di prima che mi provocava un tempo esponenziale)



def ricerca_dicotomica_disordinata(lista, numero):
    dim = len(lista)
    if dim <= 0:
        return False
    else:
        print(lista)
        mezzo = lista[dim//2]
        if numero == mezzo:
            return True
        else: # numero > mezzo
            sx = lista[:dim//2]
            dx = lista[dim//2 + 1:]
            return ricerca_dicotomica_disordinata(sx, numero) or ricerca_dicotomica_disordinata(dx, numero)

n = 20
print("\nRicerca dicotomica lista disordinata, cerco", n)
from random import randint
lista = [randint(0,50) for _ in range(20)]
lista.sort()
# print(lista)
print(ricerca_dicotomica_disordinata(lista, 20))
     
# qui il tempo non è logaritmico, rimane lineare ma anche se la funzione richiama se stessa 2 volte, lo fa
# per parti della lista sempre diverse