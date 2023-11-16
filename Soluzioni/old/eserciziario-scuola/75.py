# 75.	Funzione che dato il tempo di caduta di un oggetto,
# calcola l'altezza da cui è caduto l'oggetto e la velocità  di impatto.
# Le formule che ti servono sono: h = 1/2 * g * t^2, con g=9,81 e v=g*t.
# Almeno uno dei due valori deve essere restituito normalmente

def altezza_e_velocita(t):
    return (1/2*9.81*t**2, 9.81*t)


t = 1
h, v = altezza_e_velocita(t)
print(
    f"Se il tempo di caduta è {t} secondi, allora l'oggetto è caduto di {h} metri e ha urtato il suolo ad una velocità di {v} m/s")
