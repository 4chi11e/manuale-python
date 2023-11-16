# 6.13	Scrivi un programma che legga i dati contenuti in un file di testo (testo riportato di seguito) e li inserisca in opportune strutture dati che rappresentino il registro dei voti per una materia. Il programma deve poi calcolare la media dei voti per ogni singolo studente e aggiungerla alla struttura dati (che quindi conterrà anche una variabile media). Il programma deve mostrare tutti i dati raccolti e calcolati sullo schermo e salvarli in un secondo file di testo. Questa versione del programma è più difficile della precedente perché si può notare che i cognomi possono essere formati da più parole e sono separati dai voti da un “:”, inoltre il numero di voti varia per ogni studente.

from statistics import mean

class Studente:
    def __init__(self, cognome = "", voti = []):
        self.cognome = cognome
        self.voti = voti
        self.media = mean(voti) # se no te la calcoli tu con il solito ciclo o con sum(voti) / len(voti) per cui non serve importare niente
    
    def __repr__(self) -> str:
        ris = f"{self.cognome}: "
        for voto in self.voti:
            ris += f"{voto} "
        ris += f"- Media: {self.media:.2f}"
        return ris


with open("6-13-input.txt", encoding = 'utf-8') as fi:
    studenti = []
    for riga in fi:
        dati = list(map(str.strip, riga.split(":")))
        cognome = dati[0]
        voti = list(map(str.strip, dati[1].split()))
        voti = list(map(float, voti))
        studenti.append(Studente(cognome, voti))
        # print(studenti[-1])

    for studente in studenti:
        print(studente)

    with open("6-13-output.txt", "w", encoding = 'utf-8') as fo:
        # due alternative

        # 1
        # for studente in studenti:
            # fo.write(str(studente))
            # fo.write("\n")

        # 2 (qui map non lo userei perchè va aggiunto il \n)
        fo.writelines(str(s) + '\n' for s in studenti)
