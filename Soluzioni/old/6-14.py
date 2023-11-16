# 6.14	Leggi le informazioni riguardanti una serie di libri dal file allegato "5-12-scrittori.txt" e:
# a.	carica i dati in un array di libri (definisci un'apposita struttura libro)
# b.	ordina i libri per data di scrittura e riscrivili in un altro file nello stesso formato del file originale
# c.	scrivi e usa una funzione che riceve i dati già caricati e che restituisce il libro più recente
# d.	scrivi e usa una funzione che restituisca il secolo in cui sono stati scritti più libri (possibilmente indicando anche il numero di libri)

class libro:
    def __init__(self, titolo = "", autore = "", anno = 0):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
    
    def __repr__(self) -> str:
        return f"{self.titolo};{self.autore};{self.anno}\n"


def piu_recente(libri):
    imin = 0
    min = libri[0].anno
    for i, libro in enumerate(libri):
        if libro.anno < min:
            imin = i
            min = libro.anno
    return libri[i]


def secolo_con_piu_libri(libri):
    secoli = {}
    for libro in libri:
        secolo = (libro.anno // 100) * 100
        if secolo in secoli:
            secoli[secolo] += 1
        else:
            secoli[secolo] = 1

    # print (secoli)

    smax = None
    for secolo, n in secoli.items():
        if smax == None or n > nmax:
            smax = secolo
            nmax = n
    return (smax, nmax)



with open("6-14-input.txt", encoding = 'utf-8') as fi:
    libri = []
    for riga in fi:
        # dati = [dato.strip() for dato in riga.split(";")]
        dati = list(map(str.strip, riga.split(";")))
        # print(dati)
        libri.append(libro(dati[0], dati[1], int(dati[2])))
        # print(libri[-1])

    libri.sort(key=lambda el: el.anno)
    print(libri)

    with open("6-14-output.txt", "w", encoding = 'utf-8') as fo:
        # ci sono 3 alternative
        
        # 1
        # for libro in libri:
        #     fo.write(str(libro))
        #     fo.write("\n")
        
        # 2
        # fo.writelines(str(libro) for libro in libri)
        
        # 3
        fo.writelines(map(str, libri))

    print(f"\n\nIl libro più recente è {str(piu_recente(libri))}")

    x = secolo_con_piu_libri(libri)
    print(f"\n\nIl secolo con più libri: {x[0]} con {x[1]} libri")
    # secolo_con_piu_libri(libri)
    

