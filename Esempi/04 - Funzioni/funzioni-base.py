# le funzioni non richiedono il tipo, si scrive solo def
def somma(a, b):
    return a+b

a = 2
b = 2
c = somma(a,b)
print(f"{a} + {b} = {c}")
print(f"{a} + {b} = {somma(a, b)}")

# una funzione può restituire più valori per mezzo di liste, tuple, dizionari...
def primi_10_numeri():
    return [i for i in range(1,11)]

print(primi_10_numeri())

# una funzione può non resituire nulla
def stampa(lista):
    for el in lista:
        print(el, end=" ")

stampa(primi_10_numeri())
print()