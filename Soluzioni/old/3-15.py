# 3.14	Leggi una stringa da input e poi comunica all’utente di quante lettere è composta la stringa. Il conteggio deve essere fatto in due modi diversi, usando la funzione len e contando i caratteri uno alla volta.

s = input("Scrivi qualcosa: ")

print(f"La stringa \"{s}\" è formata da {len(s)} caratteri")

lung = 0
for lettera in s:
    lung += 1

print(f"La stringa \"{s}\" è formata da {lung} caratteri")