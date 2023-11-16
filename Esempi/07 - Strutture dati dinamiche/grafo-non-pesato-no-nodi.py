from coda import Coda

class Grafo:
    def __init__(self, nodi = [], archi = []) -> None:
        self.nodi = nodi
        self.archi = archi

    def __repr__(self) -> str:
        ris = f'Nodi: {self.nodi}\n'
        ris = f'Archi: {self.archi}\n'
        return ris

    def raggiungibile(self, a, b):
        if (a < 0 or a >= len(self.nodi)) or (b < 0 or b >= len(self.nodi)):
            return False
        if a == b:
            return True

        # controllati = []
        # controllare = []
        # controllare.append(a)

        # while (len(controllare) > 0):
        #     controllo = controllare[0]
        #     controllare.pop(0)
        #     for pos, peso in self.nodi[controllo].archi:
        #         if pos == b:
        #             return True
        #         else:
        #             if pos not in controllati and pos not in controllare:
        #                 controllare.append(pos)
        
        #     controllati.append(controllo)
        return False


g = Grafo([0,1,2,3,4,5], [(0,1),(1,2),(1,3),(2,3),(2,4),(3,4),(4,2),(4,0),(5,0),(5,1)])

# print(g)
# print(g.raggiungibile(2, 1))
# print(g.raggiungibile(2, 5))

    