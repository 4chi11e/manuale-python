class Pila:
    def __init__(self) -> None:
        self.dati = []

    def push(self, dato):
        self.dati.append(dato)

    def pop(self):
        self.dati.pop()

    def top(self):
        if len(self.dati) > 0:
            return self.dati[-1]
        else: 
            return None
    
    def empty(self):
        return len(self.dati) == 0




