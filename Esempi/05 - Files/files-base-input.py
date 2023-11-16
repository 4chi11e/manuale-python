# https://www.programiz.com/python-programming/file-operation

print("1 ------------------------------------------------------")
with open("files-base-input.txt",'r',encoding = 'utf-8') as f:
    for riga in f:
        print(riga, end="") # notare che vengono letti anche i \n e quindi mi va a capo quando stampo


print("\n\n2 ------------------------------------------------------")
with open("files-base-input.txt",'r',encoding = 'utf-8') as f:
    riga = f.readline()
    print(riga, end="")
    riga = f.readline()
    print(riga, end="")
    riga = f.readline()
    print(riga, end="")
    riga = f.readline() # qui non legge nulla perchè il file è finito
    print(riga, end="")


print("\n\n3 ------------------------------------------------------") 
with open("files-base-input.txt",'r',encoding = 'utf-8') as f:
    testo = f.read()
    print(testo)


print("\n\n4 ------------------------------------------------------") 
with open("files-base-input.txt",'r',encoding = 'utf-8') as f:
    righe = f.readlines()
    print(righe)
    for riga in righe:
        print(riga, end="")

    print("\n\n5 ------------------------------------------------------") 
    print(f.tell()) # posizione nel file
    f.seek(0) # posiziono il cursore a 0, prevede anche il parametro from, vedi sito
    print(f.tell())
    testo = f.read() # rilegge quindi dall'inizio
    print(testo)
