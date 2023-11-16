from coda import Coda

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

    def raggiungibile(self, a, b):
        if (a < 0 or a >= len(self.nodi)) or (b < 0 or b >= len(self.nodi)):
            return False
        if a == b:
            return True

        controllati = []
        controllare = []
        controllare.append(a)

        while len(controllare) > 0:
            controllo = controllare[0]
            controllare.pop(0)
            for pos, peso in self.nodi[controllo].archi:
                if pos == b:
                    return True
                else:
                    if pos not in controllati and pos not in controllare:
                        controllare.append(pos)
        
            controllati.append(controllo)
        return False


    def distanze(self, orig, dest = None):
        if orig < 0 or orig >= len(self.nodi):
            return None
        if dest != None and (dest < 0 or dest >= len(self.nodi)):
            return None

        # lista delle distanze di ogni nodo da orig
        # all'inizio sono tutte sconosciute (None)
        dist = [None for _ in range(len(self.nodi))]
        # tranne l'origine che ha distanza 0 da se stessa
        dist[orig] = 0

        # lista in cui segno per ogni nodo da quale altro nodo 
        # ci arrivo nel percorso ottimo (all'inizio è tutto sconosciuto)
        prec = [None for _ in range(len(self.nodi))]

        # nodi da controllare
        controllare = [orig]
        controllati = []

        # # nodo da cui partire
        # corrente = orig

        while len(controllare) > 0:
            # scelgo il prossimo nodo da controllare (corrente)
            # trovo il nodo con distanza minima in controllare
            corrente = controllare[0]
            for nodo in controllare:
                if dist[nodo] < dist[corrente]:
                    corrente = nodo

            # controllo tutti i nodi raggiungibili da corrente con i suoi archi
            for pos, peso in self.nodi[corrente].archi:
                # ogni nodo che raggiungo da corrente con il minor costo visto finora 
                # per quel nodo va aggiornato (distanza ottima e nodo precedente nel 
                # percorso ottimo) e aggiunto a controllare 
                if dist[pos] == None or dist[corrente] + peso < dist[pos]:
                    dist[pos] = dist[corrente] + peso
                    prec[pos] = corrente
                    if pos not in controllare and pos not in controllati:
                        controllare.append(pos)

            # rimuovo da controllare il nodo corrente, qui non ci potrò mai più 
            # tornare perchè è impossibile che possa tornarci con distanza minore 
            # di ora perchè quando scelgo il nodo da controllare prendo sempre 
            # quello con distanza minima
            controllare.remove(corrente)
            controllati.append(corrente)
        
        # caso in cui non specifico una destinazione
        # restituisco tutte le distanze e i nodi precedenti per ogni nodo
        if dest == None:
            return (dist, prec)
        # caso in cui specifico un nodo destinazione
        # restituisco la singola distanza e tutto il percorso da orig a dest
        else:

            # se il nodo dest non è raggiungibile
            if dist[dest] == None:
                percorso = []
            # altrimenti ricostruisco il percorso a ritroso da dest a orig
            else:
                percorso = [dest]
                pos = dest
                while prec[pos] != None:
                    pos = prec[pos]
                    percorso.append(pos)
                percorso = percorso[::-1]
            
            return (dist[dest], percorso)





g = Grafo()
g.nodi.append(Nodo(0, [(1,1)]))
g.nodi.append(Nodo(1, [(2,5), (3, 2)]))
g.nodi.append(Nodo(2, [(3,1), (4, 3)]))
g.nodi.append(Nodo(3, [(4,1), (1, 4)]))
g.nodi.append(Nodo(4, [(2,1), (0, 3)]))
g.nodi.append(Nodo(5, [(0,4), (4, 1)]))

print(g)
# print(g.raggiungibile(2, 1))
# print(g.raggiungibile(2, 5))

print(g.distanze(0))

    