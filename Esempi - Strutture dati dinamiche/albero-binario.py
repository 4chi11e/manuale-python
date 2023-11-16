class Nodo:
    def __init__(self, val, sx = None, dx = None) -> None:
        self.val = val
        self.sx = sx
        self.dx = dx

    def __repr__(self) -> str:
        return f'{self.val}'

    def contiene(self, val):
        if self.val == val:
            return True
        else:
            return (self.sx != None and self.sx.contiene(val)) or (self.dx != None and self.dx.contiene(val))

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
    


    
radice = Nodo(1)
radice.sx = Nodo(2)
radice.dx = Nodo(3)
radice.sx.sx = Nodo(5)
radice.sx.dx = Nodo(7)

print(radice.alberoToString())

a = Nodo(1)
a1 = Nodo(2, Nodo(5), Nodo(7))
print(a1.alberoToString())
a2 = Nodo(3, Nodo(4))
print(a2.alberoToString())
a.sx = a1
a.dx = a2
print(a.alberoToString())

print(a.contiene(3))
print(a.contiene(30))