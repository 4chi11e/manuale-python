# 6.	Data la seguente stringa stampa:
stringa = "   Vediamo come me la CAVO   "   # attento che ci sono spazi extra alla fine e all'inizio

#     1. La stringa così com'è
#     2. La stringa rimuovendo eventuali spazi iniziali e finali
#     3. La stringa nella versione con tutte le lettere minuscole
#     4. La stringa nella versione con tutte le lettere maiuscole
#     5. La stringa con la sola prima lettera maiuscola
#     6. La stringa con le sole prime lettere di ogni parola maiuscole
#     7. La seconda parola della stringa
#     8. La stringa ottenuta sostituendo tutte le 'a' con delle 'e'


#     1. La stringa così com'è
print(stringa)


#     2. La stringa rimuovendo eventuali spazi iniziali e finali
# uso quindi le funzioni
# strip(): returns a new string after removing any leading and trailing whitespaces including tabs (\t). - comprende le altre due
# rstrip(): returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
# lstrip(): returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.

# print(len(stringa))
stringa = stringa.strip()
# print(len(stringa))
print(stringa)


#     3. La stringa nella versione con tutte le lettere minuscole
print(stringa.lower())


#     4. La stringa nella versione con tutte le lettere maiuscole
print(stringa.upper())


#     5. La stringa con la sola prima lettera maiuscola
print(stringa.capitalize())

#     6. La stringa con le sole prime lettere di ogni parola maiuscole
lista = stringa.split()
lista = list(map(str.capitalize, lista))
print(" ".join(lista))


#     7. La seconda parola della stringa
print(stringa.split()[1])


#     8. La stringa ottenuta sostituendo tutte le 'a' con delle 'e'
print(stringa.replace('a', 'e')) # così funziona solo con le minuscole
tmp = stringa.replace('a', 'e')
tmp = tmp.replace('A', 'E')
print(tmp)