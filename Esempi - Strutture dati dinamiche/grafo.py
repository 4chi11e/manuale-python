class Nodo:
    def __init__(self, val, archi = None) -> None:
        self.val = val
        if archi == None:
            self.archi = []
        else:
            self.archi = archi

class Grafo:
    def __init__(self, nodi = None) -> None:
        if nodi == None:
            self.nodi = []
        else:
            self.nodi = nodi

    def __repr__(self) -> str:
        ris = ''
        for i, nodo in enumerate(self.nodi):
            ris += f'{i}. {nodo.val} : '
            for arco in nodo.archi:
                ris += f'{arco} '
            ris += '\n'
        return ris

g = Grafo([Nodo(1, [1,2])])

g.nodi.append(Nodo(5, [2]))
g.nodi.append(Nodo(3, [0]))
g.nodi[2].archi.append(1)

print(g)

    