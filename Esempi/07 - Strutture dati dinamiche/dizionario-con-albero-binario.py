class NodoDizionario:
    def __init__(self, key, val, sx = None, dx = None) -> None:
        self.key = key
        self.val = val
        self.sx = sx
        self.dx = dx

    def __repr__(self) -> str:
        return f'{self.val}'

    def push(self, nodo):
        if nodo.key <= self.key:
            if self.sx == None:
                self.sx = nodo
            else:
                self.sx.push(nodo)
        else:
            if self.dx == None:
                self.dx = nodo
            else:
                self.dx.push(nodo)

    def contiene(self, key):
        if self.key == key:
            return True
        else:
            if key <= self.key:
                return self.sx != None and self.sx.contiene(key)
            else:
                return self.dx != None and self.dx.contiene(key)

    # questa funzione l'ho aggiunta solo per vedere la struttura dell'albero, non serve
    def alberoToString(self, prof = 1):
        ris = f'{self.key}: {self.val}'
        if self.sx != None or self.dx != None:
            ris += '\n'
        if self.sx != None:
            for _ in range(prof):
                ris += '   '
            ris += 'sx: '
            ris += self.sx.alberoToString(prof+1)
            # ris += '\n'
        if self.dx != None:
            for _ in range(prof):
                ris += '   '
            ris += 'dx: '
            ris += self.dx.alberoToString(prof+1)
            # ris += '\n'
        # print(ris)
        if self.sx == None and self.dx == None:
            ris += '\n'
        return ris
    

class Dizionario:
    def __init__(self, radice = None) -> None:
        self.radice = radice

    def __repr__(self) -> str:
        if self.radice == None:
            return '{}'
        else:
            ris = '{'
            ris += ', '.join(self.contenuto(self.radice))
            ris += '}'
            return ris
        
    # repr ha bisogno di una funzione ricorsiva sui nodi
    def contenuto(self, nodo):
        ris = [f'{nodo.key}: {nodo.val}']
        if nodo.sx != None:
            ris += self.contenuto(nodo.sx)
        if nodo.dx != None:
            ris += self.contenuto(nodo.dx)
        return ris

    def __contains__(self, key):
        if self.radice == None:
            return False
        else:
            return self.radice.contiene(key)

    def __getitem__(self, key):
        if key in self:
            return self.getValNodo(self.radice, key)
        else:
            raise Exception("Chiave inesistente")
        
    # getitem ha bisogno di una funzione ricorsiva sui nodi
    def getValNodo(self, nodo, key):
        if nodo == None: # non serve per come è fatta la funzione getitem, ma controllare non fa male
            return
        if nodo.key == key:
            return nodo.val
        elif key < nodo.key:
            return self.getValNodo(nodo.sx, key)
        else:
            return self.getValNodo(nodo.dx, key)
        
    def __setitem__(self, key, val):
        if key in self:
            self.modificaNodo(self.radice, key, val)
        else:
            if self.radice == None:
                self.radice = NodoDizionario(key, val)
            else:
                self.radice.push(NodoDizionario(key, val))

    # setitem ha bisogno di una funzione ricorsiva sui nodi
    def modificaNodo(self, nodo, key, val):
        if nodo == None:
            return
        if nodo.key == key:
            nodo.val = val
        elif key < nodo.key:
            self.modificaNodo(nodo.sx, key, val)
        else:
            self.modificaNodo(nodo.dx, key, val)

    # molto simile a repr
    def items(self):
        ris = []
        ris += self.itemsR(self.radice)
        return ris
        
    # anche items ha bisogno di una funzione ricorsiva sui nodi
    def itemsR(self, nodo):
        ris = [(nodo.key, nodo.val)]
        if nodo.sx != None:
            ris += self.itemsR(nodo.sx)
        if nodo.dx != None:
            ris += self.itemsR(nodo.dx)
        return ris
    

    

d = Dizionario()
d[5] = 4
d[2] = 3
d[3] = 3
d[7] = 3
d[8] = 3
d[6] = 3

print(d)
print(d[7])
print(d.items())

