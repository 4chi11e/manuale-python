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
        
    @staticmethod
    def alberoDaFile(nomefile):
        with open(nomefile) as f:
            riga = f.readline().strip()
            if len(riga) == 0:
                root = None
            else:
                root = Nodo(riga)
                nodi = [root]
                for prof, riga in enumerate(f):
                    prof += 1
                    print(prof, riga)
                    riga = riga.strip().split('-')
                    nodi2 = []
                    for i, figli in enumerate(riga):
                        figli = figli.split()
                        figli = [Nodo(figlio) for figlio in figli]
                        nodi[i].figli = figli
                        nodi2 += figli
                    nodi = nodi2
        return root

root = Nodo.alberoDaFile('albero-da-file.txt')
print(root.getAlbero())