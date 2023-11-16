class Nodo:
    def __init__(self, val, sx = None, dx = None) -> None:
        self.val = val
        self.sx = sx
        self.dx = dx

    def __repr__(self) -> str:
        return f'{self.val}'

    def push(self, nodo):
        if nodo.val <= self.val:
            if self.sx == None:
                self.sx = nodo
            else:
                self.sx.push(nodo)
        else:
            if self.dx == None:
                self.dx = nodo
            else:
                self.dx.push(nodo)

    def contiene(self, val):
        if self.val == val:
            return True
        else:
            if val <= self.val:
                return self.sx != None and self.sx.contiene(val)
            else:
                return self.dx != None and self.dx.contiene(val)

    def alberoToString(self, prof = 1):
        ris = f'{self.val}'
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
    


    
radice = Nodo(5)
radice.push(Nodo(2))
radice.push(Nodo(3))
radice.push(Nodo(5))
radice.push(Nodo(7))
radice.push(Nodo(6))
radice.push(Nodo(9))

print(radice.alberoToString())

print(radice.contiene(3))
print(radice.contiene(30))
