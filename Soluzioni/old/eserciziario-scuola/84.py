# 8.1.1	Scrivi un programma che utilizzi una funzione che, ricevuto un array di numeri interi, restituisce il numero che compare con più frequenza (in caso di parità restituisce il primo numero trovato con la frequenza maggiore). Puoi risolvilo in due modi:
# 1.	Con sole liste (inutilmente complicato e fattibile in vari modi complicati)
# 2.	Con un dizionario


def numero_con_frequenza_massima_lista(numeri):
    frequenze = [0 for _ in range(len(numeri))]
    for i in range(len(numeri)):
        if frequenze[i] == 0:
            frequenze[i] = 1
            for j in range(i+1, len(numeri)):
                if(numeri[i] == numeri[j]):
                    frequenze[i] += 1
                    frequenze[j] += 1
    
    val_max = frequenze[0]
    pos_max = 0
    for i in range(1, len(numeri)):
        if frequenze[i] > val_max:
            val_max = frequenze[i]
            pos_max = i

    return numeri[pos_max]


def numero_con_frequenza_massima_dizionario(numeri):
    frequenze = {}
    freq_max = 1
    num_max = numeri[0]
    for num in numeri:
        if num in frequenze:
            frequenze[num] += 1
        else:
            frequenze[num] = 1
        if frequenze[num] > freq_max:
            freq_max = frequenze[num]
            num_max = num
    return num_max


numeri = [1,1,2,2,2,3,4,8,6,4,4]
print(numeri)
print("Primo numero con frequenza massima (liste):", numero_con_frequenza_massima_lista(numeri))
print("Primo numero con frequenza massima (dizionario):", numero_con_frequenza_massima_dizionario(numeri))
