import random

def bubble_sort(V):
    for i in range(len(V)-1):
        for j in range(len(V)-1-i):
            if V[j] > V[j+1]:
                V[j], V[j+1] = V[j+1], V[j]


# V = [random.randint(0, 10) for _ in range(10)]

# print(V)
# bubble_sort(V)
# print(V)