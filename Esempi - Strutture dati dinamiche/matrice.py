class Matrice2d:
    def __init__(self, dati) -> None:
        self.dati = dati

    def __repr__(self) -> str:
        ris = '['

        # per stampare bene cerco la larghezza delle colonne
        dimcolonne = []
        for riga in self.dati:
            for j, dato in enumerate(riga):
                if len(dimcolonne) <= j:
                    dimcolonne.append(1)
                if dimcolonne[j] < len(f'{dato}'):
                    dimcolonne[j] = len(f'{dato}')
        
        for i, riga in enumerate(self.dati):
            tmp = []
            for j, dato in enumerate(riga):
                l = len(f'{dato}')
                spazi = ' '*(dimcolonne[j]-l)
                tmp.append(f'{spazi}{dato}')
            if i == 0:
                spazio = ''
            else:
                spazio = ' '
            tmp = spazio + ', '.join(tmp)
            if i == len(self.dati)-1:
                ris += tmp+']\n'
            else:    
                ris += tmp+'\n'

        return ris    
    

from random import randint    
m = Matrice2d([[randint(0,10)**randint(0,5) for _ in range(4)] for _ in range(6)])
print(m.dati)
print()
print(m)