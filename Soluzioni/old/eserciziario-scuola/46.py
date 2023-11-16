# 46.	Leggi una stringa da input e poi comunica all’utente di 
# quante lettere è composta la stringa. Il conteggio deve essere 
# fatto in due modi diversi, usando la funzione strlen e contando 
# i caratteri uno alla volta.

stringa = input("Scrivi qualcosa: ")

# print(stringa)

numero_lettere = 0
for lettera in stringa:
    numero_lettere += 1

print(f"Contando i caratteri uno alla volta ho contato {numero_lettere} lettere")

numero_lettere = len(stringa)
print(f"\nContando i caratteri con la funzione len ho contato {numero_lettere} lettere")
