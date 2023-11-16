# 88.	Scrivi e utilizza una funzione che calcola il quoziente tra due numeri interi 
# e restituisce, oltre al quoziente anche il resto della divisione.

def divisione_intera(a,b):
    quoziente = a // b
    resto = a % b
    return (quoziente, resto)

a = 22
b = 3
q, r = divisione_intera(a,b)
print(f"{a}/{b} = {q} resto {r}")
