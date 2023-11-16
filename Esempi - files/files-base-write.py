# https://www.programiz.com/python-programming/file-operation

# anche qui è prevista la modalita 'w' write e la modalità 'a' append

with open("files-base-output.txt",'w',encoding = 'utf-8') as f: # il file viene creato se non esiste
    f.write("Ciao bellissimi, ")
    f.write("come state?\n")
    f.write("Bene, grazie!")

with open("files-base-output.txt",'a',encoding = 'utf-8') as f: # append aggiunge alla fine
    f.write("\nNuova riga aggiunta al file.")

# with open("files-base-output.txt",'w',encoding = 'utf-8') as f: # il file viene sovrascritto se già esiste
#     f.write("Così cancello tutte le cose vecchie.")


with open("files-base-output2.txt",'w',encoding = 'utf-8') as f:
    lista = [f"riga {i}\n" for i in range(1,6)]
    f.writelines(lista)
