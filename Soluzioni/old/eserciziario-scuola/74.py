# 74.	Funzione che date le coordinate di due punti nel piano, 
# calcolino e restituiscano le coordinate del punto medio 	
# tra i due (senza approssimazioni).

def punto_medio(a, b):
    medio = ((a[0]+b[0])/2, (a[1]+b[1])/2)
    return medio

a=(1,2)
b=(2,2)
print(punto_medio(a,b))
