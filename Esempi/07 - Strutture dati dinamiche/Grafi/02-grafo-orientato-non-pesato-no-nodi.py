class Grafo:
    def __init__(self, nodi = None, archi = None) -> None:
        self.nodi = nodi
        if nodi == None:
            self.nodi = []
        self.archi = archi
        if archi == None:
            self.archi = []

    def __repr__(self) -> str:
        ris =  f'Nodi:  {self.nodi}\n'
        ris += f'Archi: {self.archi}\n'
        return ris


# i valori dei nodi li ho inseriti uguali alle posizioni nella lista per non confondersi
# gli archi si possono ripetere invertiti perchè sono orientati
go = Grafo(
    [0, 1, 2, 3, 4, 5],
    [
        (0, 1),
        (1, 2),
        (1, 3),
        (2, 3),
        (2, 4),
        (3, 1),
        (3, 4),
        (4, 0),
        (4, 2),
        (5, 0),
        (5, 4),
    ],
)
print(go)


    