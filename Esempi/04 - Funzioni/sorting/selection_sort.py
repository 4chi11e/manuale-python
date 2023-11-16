import random

def selection_sort(V):
    for i in range(len(V)-1):
        jmin = i
        for j in range(i+1, len(V)):
            if V[j] < V[jmin]:
                jmin = j


# V = [random.randint(0, 10) for _ in range(10)]

# print(V)
# selection_sort(V)
# print(V)