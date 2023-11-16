# 1.1	Dati in input due numeri, scrivi il risultato di tutte le operazioni che è possibile fare con i due numeri 
# (somma, sottrazione, moltiplicazione, divisione intera, resto della divisione, divisione con decimali, potenza)


a = int(input("Scrivi il primo numero: "))
b = int(input("Scrivi il secondo numero: "))

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} ** {b} = {a**b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")