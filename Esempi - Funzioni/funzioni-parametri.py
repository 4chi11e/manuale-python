import os;
os.system('cls')


# i parametri vengono passati per riferimento, una sorta di versione semplificata dei puntatori
def aggiungi(v, x):
    v.append(x)

lista = [1,2,3]
aggiungi(lista, 4)
print(lista)
# lista non viene copiato, viene passato un riferimento all'originale quindi lo posso modificare


# chiamare un metodo (o funzione, nel caso precedente append) di un oggetto può modificare l'oggetto 
# ma non il riferimento all'oggetto; se invece riassegno qualcosa alla variabile, 
# python ridichiara la variabile e perdo il riferimento originale

def raddoppia(x):
    x = x*2 # anche se facessi *=

a = 2
raddoppia(a)
print(a)
# a vale ancora 2

# se voglio modificare una variabile semplice la restituisco
def raddoppia(x):
    return x*2

a = 2
a = raddoppia(a)
print(a)


# questo comportamento è strano per chi è abituato a C o C++, ma è abbastanza comodo se ci si fa l'abitudine.
# normalmente modifico le strutture e restituisco valori singoli.

# una classe (nativa o da me definita) funziona come una qualsiasi variabile semplice: 
# per modificarla uso i suoi metodi e non perdo il riferimento
# se la riassegno perdo il riferimento originale

def aggiungi2(v, x):
    v = [1,2,3,x]

lista = [1,2,3]
aggiungi2(lista, 4)
print("lista:", lista)



