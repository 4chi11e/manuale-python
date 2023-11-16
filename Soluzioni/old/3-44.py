# 3.44	Scrivi un programma che permetta di rappresentare il campo di gioco di “Campo minato”. 
# Il campo deve essere formato da una superficie suddivisa in caselle quadrate, quindi avrai una 
# grande tabella (ad esempio di dimensioni 8x12 ma puoi scegliere diversamente). Sul campo devono 
# essere disposte a caso una serie di mine (suggerisco 16 ma puoi cambiare). Fai poi in modo che 
# ogni casella che non sia una mina abbia un numero che rappresenti il numero di mine adiacenti 
# (anche in diagonale quindi un numero da 1 a 8) lasciando vuote le celle che non hanno mine adiacenti 
# (non scrivere 0) 

# sviluppo questo programma senza creare classi

import random

nmine = 16
nrighe = 8
ncolonne = 12
vuoto = " "
mina = "X"


campo = [[vuoto for j in range(ncolonne)] for i in range(nrighe)]
for _ in range(nmine):
    i = random.randint(0, nrighe-1)
    j = random.randint(0, ncolonne-1)
    while (campo[i][j] != " "):
        i = random.randint(0, nrighe-1)
        j = random.randint(0, ncolonne-1)
    campo[i][j] = mina

for i in range(nrighe):
    for j in range(ncolonne):
        if campo[i][j] != mina:
            val = 0
            if i > 0        and j > 0           and campo[i-1][j-1] == mina:        # ↖
                val +=1
            if i > 0                            and campo[i-1][j] == mina:          # ↑
                val +=1
            if i > 0        and j < ncolonne-1  and campo[i-1][j+1] == mina:        # ↗
                val +=1
            if                  j < ncolonne-1  and campo[i][j+1] == mina:          # →
                val +=1
            if i < nrighe-1 and j < ncolonne-1  and campo[i+1][j+1] == mina:        # ↘
                val +=1
            if i < nrighe-1                     and campo[i+1][j] == mina:          # ↓
                val +=1
            if i < nrighe-1 and j > 0           and campo[i+1][j-1] == mina:        # ↙
                val +=1
            if                  j > 0           and campo[i][j-1] == mina:          # ←
                val +=1
        
            if val > 0:
                campo[i][j] = val
        
        print(campo[i][j], end = " ")
    print()
        
# ←	↑	→	↓	↔	↕	↖	↗	↘	↙

