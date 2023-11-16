# https://it.wikipedia.org/wiki/Quicksort
# https://www.youtube.com/watch?v=dV-JgquCwHo

import random

def partition(V, a, b):
    sx = a
    dx = b
    pivot = dx
    while sx < dx:
        if pivot == dx:
            if V[pivot] >= V[sx]:
                sx += 1
            else:
                V[pivot], V[sx] = V[sx], V[pivot]
                pivot = sx
        else:
            if V[pivot] <= V[dx]:
                dx -= 1
            else:
                V[pivot], V[dx] = V[dx], V[pivot]
                pivot = dx
    return pivot


def quick_sort(V, a = 0, b = None):
    if type(V) != list:
        print("errore, non hai passato una lista")
        return None
    if b == None:
        b = len(V) - 1
    if b-a <= 0:
        return
    else:
        pivot = partition(V, a, b)
        quick_sort(V, a, pivot-1)
        quick_sort(V, pivot+1, b)
    

# V = [random.randint(0, 10) for _ in range(10)]
# # V = [3,1,6,4,2]

# print(V)
# quick_sort(V)
# print(V)
