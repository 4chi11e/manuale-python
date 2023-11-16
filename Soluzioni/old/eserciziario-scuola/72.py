# 4.1.4	Quando possibile, scrivi e utilizza le seguenti funzioni:
# 1. raddoppia un numero passando parametri per valore,
# 2. raddoppia un numero passando parametri per indirizzo,
# 3. raddoppia due numeri contemporaneamente.


# 1. raddoppia un numero passando parametri per valore,

# il passaggio è sempre per riferimento ma se riassegno la variabile perdo il riferimento alla variabile originale
# è quindi possibile solo restituire il doppio  
def raddoppia(x):
    x *= 2
    return x

a = 5
a = raddoppia(a)
print("1.", a)


# 2. raddoppia un numero passando parametri per indirizzo,

# il passaggio è sempre per riferimento ma se riassegno la variabile perdo il riferimento alla variabile originale
# vediamo che cosa succede se provo a farlo
def raddoppia2(x):
    x *= 2

a = 5
raddoppia2(a)
print("2.", a)

# 3. raddoppia due numeri contemporaneamente.
# quello che posso fare è passare una struttura dati iterabile e raddoppiare tutti i valori in essa contenuti,
# in questo caso non modifico il riferimento alla struttura originale ma solo il contenuto
def raddoppia3(v):
    for i in range(len(v)):
        v[i] *=2


# a = (2, 3) # attento con una tupla non lo puoi fare, la tupla è immodificabile
a = [2, 3]
raddoppia3(a)
print("3.", a)


