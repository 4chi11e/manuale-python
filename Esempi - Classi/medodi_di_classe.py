# https://www.programmareinpython.it/video-corso-python-programmazione-a-oggetti/03-ereditarieta/
# https://www.programmareinpython.it/video-corso-python-programmazione-a-oggetti/04-i-metodi-di-classe/

import os;
os.system('cls')

class Persona:

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    # # versione non ereditabile
    # @classmethod
    # def from_string(cls, stringa_persona):
    #     nome, cognome, età, residenza = stringa_persona.split("-")
    #     return cls(nome, cognome, età, residenza)
    
    # versione ereditabile
    @classmethod 
    def from_string(cls, stringa_persona, *args):
        nome, cognome, età, residenza = stringa_persona.split("-") 
        return cls(nome, cognome, età, residenza, *args)


    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        return scheda

    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")
        scelta = input("Cosa Desideri modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome--> ")
        elif scelta == "2":
            self. cognome = input("Nuovo Cognome --> ")
        elif scelta == "3":
            self.età = int(input("Nuova età --> "))
        elif scelta == "4":
            self.residenza = input("Nuova Residenza --> ")


# versioni base che ereditano tutto
class Studente(Persona):
    pass


class Insegnante(Persona):
    pass


#versioni modificate che fanno l'override delle funzioni ereditate
class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio

    def scheda_personale(self):
        scheda = f"""
        Profilo: {Studente.profilo}
        Corso di Studi: {self.corso_di_studio}
        ***"""
        return super().scheda_personale() + scheda

    def cambio_corso(self,corso):
        self.corso_di_studio = corso
        print(f"Corso Aggiornato")


class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self, nome, cognome, età, residenza, materie=None):
        super().__init__(nome, cognome, età, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f"""
        Profilo: {Insegnante.profilo}
        Materie Insegnate: {self.materie}
        ***"""
        return super().scheda_personale() + scheda

    def aggiungi_materia(self,nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print("Elenco Aggiornato")




iron_man = "Tony-Stark-40-Torre Stark"
zuck = "Mark-Zuckerberg-33-California"

persona_uno = Persona.from_string(iron_man)
print(persona_uno.scheda_personale())

insg_uno = Insegnante.from_string(iron_man,"Ingegneria")
stud_uno = Studente.from_string(zuck,"SEO")

print(insg_uno.scheda_personale())
print(stud_uno.scheda_personale())