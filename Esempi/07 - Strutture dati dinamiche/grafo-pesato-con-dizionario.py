from coda import Coda
from random import randint

class Nodo:
    def __init__(self, val, archi = []) -> None:
        self.val = val
        self.archi = archi

class Grafo:
    def __init__(self, nodi = {}) -> None:
        self.nodi = nodi

    def __repr__(self) -> str:
        ris = ''
        for key, nodo in self.nodi.items():
            ris += f'{key}. {nodo.val} : '
            for arco in nodo.archi:
                ris += f'{arco} '
            ris += '\n'
        return ris
    
    def aggiungi(self, nodo, key = None):
        if key == None:
            key = 1
            while key in self.nodi:
                key += 1
        
        self.nodi[key] = nodo

    def rimuovi(self, key):
        if key not in self.nodi:
            return
        
        self.nodi.pop(key)

        for k, nodo in self.nodi.items():
            for i, arco in enumerate(nodo.archi):
                if arco[0] == key:
                    nodo.archi.pop(i)


    def raggiungibile(self, a, b):
        # a e b sono chiavi che identificano nodi in self.nodi
        if (a not in self.nodi) or (b not in self.nodi):
            return False
        if a == b:
            return True

        controllati = []
        controllare = []
        controllare.append(a)

        while (len(controllare) > 0):
            controllo = controllare[0]
            for pos, peso in self.nodi[controllo].archi:
                if pos == b:
                    return True
                else:
                    if pos not in controllati and pos not in controllare:
                        controllare.append(pos)
        
            controllare.pop(0)
            controllati.append(controllo)
        return False


g = Grafo()
g.aggiungi(Nodo(randint(0,9), [(2,1)]), 1)
# g.aggiungi(Nodo(randint(0,9), [{"key": 2, "peso": 1}]))
g.aggiungi(Nodo(randint(0,9), [(3,1), (4, 1)]))
g.aggiungi(Nodo(randint(0,9), [(4,1), (5, 1)]))
g.aggiungi(Nodo(randint(0,9), [(5,1), (2, 1)]))
g.aggiungi(Nodo(randint(0,9), [(3,1), (1, 1)]))
g.aggiungi(Nodo(randint(0,9), [(1,1), (5, 1)]))
g.nodi[1].archi.append((3,1))

print(g)
g.rimuovi(1)
print(g)

print(g.raggiungibile(2, 1))
print(g.raggiungibile(2, 5))
print(g.raggiungibile(2, 6))

    