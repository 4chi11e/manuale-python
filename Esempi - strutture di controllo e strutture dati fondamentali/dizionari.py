# un dizionario associa ad elementi detti chiave (key) dei valori (value)
d = {"Federico": 6, "Ryan": 7, "Luigi": 3}

# stampa base di tutto il dizionario
print('Stampa base del dizionario:')
print(d)
print()

# accesso ad un valore tramite la chiave
print("accesso ad un valore tramite la chiave:")
print(d["Federico"])
print()

# stampa del dizionario scorrendo tutte le chiavi
print("stampa del dizionario scorrendo tutte le chiavi: ")
for key in d:
    print(key, d[key])
print()

# la funzione items() mi restituisce tutte le coppie chiave: valore
print("stampa con items(): ")
for key, value in d.items():
    print(key, value)
print()

# posso costruire una lista di coppie (ad esempio per poi ordinarle)
print("list(d.items()):", list(d.items()))

# lista di sole chiavi
print(list(d)) # prende solo le chiavi
print()


# un dizionario può contenere anche tanti tipi diversi di dati (sconsiglio una schifezza del genere ma funziona)
d = {"Francesco": "Bellissimo", "Paolo": 15, 1: "Topolino", "pizze": ["margherita", "marinara", 12, 18]}
print("Dizionario orribile:")
print(d)
print()

# una cosa comune è avere una cosa del genere:
print("Esempio di dizionario con liste come value: ")
d = {"Battoraro": [4,5,6], "Riccobelli": [6,5,6], "Brescia": [3]}
print(d)
print()


# ordinamento di un dizionario
# i dizionari non sono ordinati, le cose rimangono nell'ordine in cui sono state ineserite
print("Dizionario poi ordinato trasformandolo in lista:")
d = {"Federico": 6, "Ryan": 7, "Luigi": 3}
print(d)
# se si vuole ordinare bisogna passare alla lista
lista = list(d.items())
lista.sort(key = lambda x: -x[1]) # qui ho ordinato per voto decrescente
d = dict(lista) # funziona quando ho una lista di tuple di 2 elementi
#equivale a
d={}
for coppia in lista:
    d[coppia[0]] = coppia[1]
print(d)





