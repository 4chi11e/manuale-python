# 3.4.6	Scrivi un programma che simuli il gioco del Black Jack. 
# Una mano del gioco è gestita da una funzione che devi chiamare manoBlackJack() che riceve come parametro una lista contenente la puntata fatta da ogni giocatore partecipante (implicitamente quindi anche il numero di giocatori) e restituisce la quantità di denaro da dare alla fine ad ogni giocatore (0 se perde, il doppio di quanto puntato se vince o lo stesso di prima se pareggia)
# La funzione deve simulare la gestione di un mazzo di carte con una opportuna struttura dati. Per semplificare il gioco la funzione manoBlackJack() utilizza un nuovo mazzo mischiato ad ogni mano (ben lontano dalla realtà).
# La funzione shuffle() consente di mescolare il mazzo (restituisce un mazzo di 52 carte pieno e mischiato)
# Sia ai giocatori che al banco, vengono assegnate inizialmente 2 carte pescate dal mazzo, entrambe scoperte per i giocatori, una coperta per il banco.
# I giocatori giocano a turno e viene chiesto loro inserire la propria decisione che può essere solo di due tipi "vedo" o "continuo". Il singolo giocatore continua a pescare carte finchè perde (somma più di 21) o decide di fermarsi. Finito il turno dei giocatori il banco gioca automaticamente secondo le regole standard del gioco (pesca fintanto che raggiunge meno di 17, da 17 in su si ferma): 

# Il programma principale chiede se un giocatore si vuole aggiungere alla partita e con quale puntata, finchè si aggiungono giocatori continua a chiederlo (massimo 7 giocatori), poi chiama la funzione per giocare una mano e alla fine chiede se i giocatori vogliono rimanere (se hanno perso ne devono mettere altri) o vogliono ritirare soldi dal tavolo (tutti e se ne vanno, una parte e rimangono). Il programma poi chiede nuovamente se ci sono nuovi giocatori che vogliono partecipare (sempre massimo 7)
# Il programma termina quanto tutti i giocatori lasciano il tavolo.


import random

valori = (1,2,3,4,5,6,7,8,9,10,'J','Q','K')
semi = ("♦♥♣♠")
mazzo_singolo = []
for seme in semi:
    for valore in valori:
        mazzo_singolo.append((valore, seme))

# mazzo_singolo = (valore, seme) for valore in valori for seme in semi

# print(mazzo_singolo)

def shuffle(nmazzi = 1):
    mazzo = []
    for _ in range(nmazzi):
        calderone = mazzo_singolo.copy()
        while len(calderone) > 0:
            i = random.randint(0, len(calderone)-1)
            mazzo.append(calderone.pop(i))

    for i in range(5):
        mazzo.pop()

    nera = random.randint(len(mazzo)*3/4, len(mazzo)*5/6)

    return mazzo, nera


# print(len(shuffle()))



