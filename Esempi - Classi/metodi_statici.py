import os;
os.system('cls')

class vettore:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, altro):
        return vettore(self.x + altro.x, self.y + altro.y)
    
    def val_assoluto(self):
        return (self.x**2 + self.y**2)**(1/2)
    
    @staticmethod
    def val_assoluto_statico(v):                # il fatto che sia statico non mi permette di avere lo stesso nome di un altra funzione normale o di classe
        return (v.x**2 + v.y**2)**(1/2)


A = vettore(0,1)
print(f"|{A}| = {A.val_assoluto()}")
print(f"|{A}| = {vettore.val_assoluto_statico(A)}")