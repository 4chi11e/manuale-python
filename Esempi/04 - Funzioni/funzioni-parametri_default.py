import os;
os.system('cls')


def stampaLista(v, orizzontale = True):
    for el in v:
        if orizzontale:
            print(el, end=" ")
        else:
            print(el)

stampaLista([1,2,3,4])
stampaLista([1,2,3,4], False)
stampaLista([1,2,3,4], orizzontale = False)

print()


# quello visto fin qui è un caso semplice, un esempio più completo può essere:
def reprPunto(nome, x = 0, y = 0):
    # questa è una funzione che riceve necessariamente il nome del punto 
    # e facoltativamente i valori delle coordinate
    return f'{nome}({x}, {y})'

print(reprPunto("A", 2, 5)) # specificare tutto va bene
print(reprPunto("B")) # se non indico i valori di x e y usa quelli di default
# print(reprPunto()) # questo non si può fare, almeno il nome va indicato perchè non ha valore di default
print(reprPunto("C", 2)) # se indico solo un valore oltre al nome lo assegna a x perchè è il primo
print(reprPunto("E", y = 5)) # se volgio indicare la y e non la x devo specificare il nome del parametro
print(reprPunto("F", x = 2, y = 5)) # posso nominarli espressamente tutti ma è inutile, posso fare comodamente come per il punto A




