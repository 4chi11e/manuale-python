# for semplici non su liste o altro

print("Numeri da 0 a 4: ")
for i in range(5):
    print(i, end=' ')
print()
print()


print("Numeri da 1 a 5: ")
for i in range(1,6):
    print(i, end=' ')
print()
print()


print("Numeri da 1 a 5 (con passo): ")
for i in range(1,6,1):  # è la versione completa con partenza, arrivo(escluso) e passo
    print(i, end=' ')
print()
print()


print("Numeri da 5 a 1: ")
for i in range(5,0,-1): # nota che il primo numero è sempre comreso il sempre escluso
    print(i, end=' ')
print()
print()


print("Numeri pari da 0 a 10: ")
for i in range(0,11,2): # nota che il primo numero è sempre comreso il sempre escluso
    print(i, end=' ')
print()
print()


