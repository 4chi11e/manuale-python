
class Lista:
    def __init__(self, dati = None) -> None:
        if dati == None:
            self.dati = []
        else:
            self.dati = dati

    def __repr__(self) -> str:
        return f'{self.dati}'
    
    def __getitem__(self, i):
        if i < 0 or i >= len(self.dati):
            return None
        else:
            return self.dati[i]
        
    def __setitem__(self, i, val):
        if i < 0 or i >= len(self.dati):
            raise Exception("indirizzo non valido")
        else:
            self.dati[i] = val
    
    def __add__(self, b):
        if type(b) == Lista:
            return Lista(self.dati + b.dati)
        elif type(b) == list:
            return Lista(self.dati + b)
        else:
            raise Exception('Ad una "Lista" puoi sommare solo altre "Lista" o "list"')

    # se deve fare la stessa cosa di __add__ non serve, come in questo caso
    # def __iadd__(self, b):
    #     if type(b) == Lista:
    #         return Lista(self.dati + b.dati)
    #     elif type(b) == list:
    #         return Lista(self.dati + b)
    #     else:
    #         raise Exception('Ad una "Lista" puoi sommare solo altre "Lista" o "list"')

        

l = Lista([1,2,3])
print(l)
print(l[1])
l[1] = 5
print(l[1])

l = Lista([1,2,3])
l = l + Lista([4, 5])
print(l)

l = Lista([1,2,3])
l = l + [4, 5]
print(l)

l = Lista([1,2,3])
l += [4, 5]
print(l)

l = Lista([1,2,3])
l = l + 5
print(l)



