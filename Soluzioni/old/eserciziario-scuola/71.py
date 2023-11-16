# 71.	Scrivi e utilizza una funzione che dati due valori 
# e un simbolo di una delle 4 operazioni effettua quella 
# operazione e restituisce il risultato

def calcola(a,b,simbolo):
    if simbolo == '+':
        return a+b
    elif simbolo == '-':
        return a-b
    elif simbolo == '*':
        return a*b
    elif simbolo == '/':
        return a/b
    else:
        print(f"Operatore \"{simbolo}\" errato")
        return 0

a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))
simbolo = (input("Inserisci l'operatore: "))

print(calcola(a,b,simbolo))

