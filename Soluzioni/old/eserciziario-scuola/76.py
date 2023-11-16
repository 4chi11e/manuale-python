# 76.	Funzione che prevede se un oggetto si rompe cadendo da una certa altezza.
# Quello che ti serve sapere è quindi l’altezza da cui cade l’oggetto e la velocità 
# massima di impatto che l’oggetto può sopportare. Le formule che ti servono sono: 
# h = 1/2 * g * t^2, con g=9,81 e v=g*t. 

def altezza_e_velocita(t):
    return (1/2*9.81*t**2, 9.81*t)


t = 2
max_v = 10
h, v = altezza_e_velocita(t)
print(
    f"Se il tempo di caduta è {t} secondi, allora l'oggetto è caduto di {h} metri e ha urtato il suolo ad una velocità di {v} m/s")

if v > max_v:
    print("L'oggetto si è rotto all'impatto")
else:
    print("Dopo l'impatto l'oggetto è ancora intero")