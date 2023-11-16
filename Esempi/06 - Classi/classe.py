# esempi di classi https://www.programmareinpython.it/video-corso-python-programmazione-a-oggetti/01-classi-e-istanze/
# lista di dunder methods https://www.tutorialsteacher.com/python/magic-methods-in-python

import os
os.system('cls')

class vettore:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, altro):
        return vettore(self.x + altro.x, self.y + altro.y)
    
    def modulo(self):
        return (self.x**2 + self.y**2)**(1/2)
    
    def __ge__(self, altro):
        return self.modulo() >= altro.modulo()
    

A = vettore(1, 2)
B = vettore(3, 7)
C = A + B
print(f"{A} + {B} = {C}")

D = vettore(0,1)
E = vettore(1,1)
print(f"|{D}| = {D.modulo()}")
print(f"|{E}| = {E.modulo():.4f}")

print(A >= B)

F = vettore(y = 6)
print(F)