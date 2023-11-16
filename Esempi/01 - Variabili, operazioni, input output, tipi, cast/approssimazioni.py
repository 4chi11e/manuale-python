# 1.2	Dato un numero decimale, ottieni e stampa:
    # a.	Valore intero approssimato per difetto
    # b.	Valore intero approssimato per eccesso
    # c.	Valore intero approssimato in maniera intelligente
    # d.	approssimazione del numero al secondo decimale
    # e.	Valore assoluto del numero


from math import ceil, floor

n = -7.67357

print(f"a. {n} intero approssimato per difetto: {int(n)}")
print(f"a. {n} intero approssimato per difetto: {floor(n)}") # devo importare math
print(f"b. {n} intero approssimato per eccesso: {ceil(n)}") # devo importare math
print(f"c. {n} intero approssimato in maniera intelligente: {round(n)}")
print(f"d. {n} intero approssimato al secondo decimale: {round(n, 2)}")
print(f"e. {n} valore assoluto del numero: {abs(n)}")