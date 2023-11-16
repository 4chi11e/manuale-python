class Coda:
    def __init__(self) -> None:
        self.dati = []
    
    def push(self, dato):
        self.dati.append(dato)
    
    def front(self):
        if len(self.dati) > 0:
            return self.dati[0]
        else:
            return None
    
    def pop(self):
        if len(self.dati) > 0:
            self.dati.pop(0)

    def empty(self):
        return len(self.dati) <= 0