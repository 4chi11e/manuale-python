class Nodo:
    def __init__(self, val, figli = None) -> None:
        self.val = val
        if  figli == None:
            self.figli = []
        else:
            self.figli = figli

    def __repr__(self) -> str:
        return f'{self.val}'

    # def get_val():
    #     pass

    def getAlbero(self, prof = 1):
        ris = f'({self.val}'
        if len(self.figli) > 0:
            ris += ', [\n'
            for i, figlio in enumerate(self.figli):
                for _ in range(prof):
                    ris += '     '
                ris += figlio.getAlbero(prof+1)
                if i < len(self.figli) - 1:
                    ris += '\n'
            ris += ']'
        ris += ')'
        # print(ris)
        return ris
    
    def contiene(self, val):
        if self.val == val:
            return True
        else:
            for figlio in self.figli:
                if figlio.contiene(val):
                    return True
            return False


    
radice = Nodo(1)
radice.figli.append(Nodo(2, []))
radice.figli.append(Nodo(3, []))
nodo = radice.figli[0]
nodo.figli.append(Nodo(5, [Nodo(1,[])]))
nodo.figli.append(Nodo(7, []))

# print(radice.figli)
# print(radice.figli[0])
# print(radice.figli[1].figli)
# for figlio in radice.figli:
#     print(figlio.figli)
print(radice.getAlbero())

print(radice.contiene(7))
print(radice.contiene(12))

