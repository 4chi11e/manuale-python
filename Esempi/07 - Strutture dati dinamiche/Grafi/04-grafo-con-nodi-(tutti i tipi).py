class Nodo:
    def __init__(self, val, archi = None) -> None:
        self.val = val
        self.archi = archi
        if archi == None:
            self.archi = []
    
    def __repr__(self) -> str:
        return f"({self.val}: {self.archi})"

class Grafo:
    def __init__(self, nodi = None) -> None:
        self.nodi = nodi
        if nodi == None:
            self.nodi = []
    
    def __repr__(self) -> str:
        ris = ""
        ris += "[\n"
        for nodo in self.nodi:
            ris = ris + " " + f"{nodo}\n"
        ris += "]"
        return ris
        
# grafo non orientato non pesato
g = Grafo([
    Nodo(0, [1,5]),
    Nodo(1, [0,2,3]),
    Nodo(2, [1,3,4]),
    Nodo(3, [1,2,4]),
    Nodo(4, [0,2,3,5]),
    Nodo(5, [0,4]),
])
print(g)
print()

# grafo orientato non pesato
go = Grafo([
    Nodo(0, [1]),
    Nodo(1, [2,3]),
    Nodo(2, [3,4]),
    Nodo(3, [1,4]),
    Nodo(4, [0,2]),
    Nodo(5, [0,4]),
])
print(go)
print()

# grafo orientato pesato
gop = Grafo([
    Nodo(0, [(1, 7)]),
    Nodo(1, [(2, 5), (3, 2)]),
    Nodo(2, [(3, 1), (4, 3)]),
    Nodo(3, [(1, 4), (4, 1)]),
    Nodo(4, [(0, 3), (2, 1)]),
    Nodo(5, [(0, 4), (4, 1)]),
])
print(gop)
print()