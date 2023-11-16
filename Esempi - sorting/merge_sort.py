# https://www.youtube.com/watch?v=HFnFhRKrhag

from heapq import merge
import random

def merge_sort_v1(V, a=0, b=None):
    if type(V) != list:
        print("errore, non hai passato una lista")
        return None
    if b == None:
        b = len(V) - 1

    if b > a:
        if b-a < 2:
            if V[a] > V[b]:
                V[a], V[b] = V[b], V[a]
        else:
            mid = (a + b) // 2
            merge_sort_v1(V, a, mid)
            merge_sort_v1(V, mid+1, b)

            merge
            i = a
            j = mid+1
            tmp = []
            for _ in range(b-a+1):
                if i > mid:
                    tmp.append(V[j])
                    j += 1
                elif j > b:
                    tmp.append(V[i])
                    i += 1
                elif V[i] <= V[j]:
                    tmp.append(V[i])
                    i += 1
                else:
                    tmp.append(V[j])
                    j += 1

            for i in range(len(tmp)):
                V[a+i] = tmp[i]

            # tmp = V[a: b+1]
            # i = 0
            # j = mid-a+1
            # for k in range(a, b+1):
            #     if i > mid-a:
            #         V[k] = tmp[j]
            #         j += 1
            #     elif j > b-a:
            #         V[k] = tmp[i]
            #         i += 1
            #     elif tmp[i] <= tmp[j]:
            #         V[k] = tmp[i]
            #         i += 1
            #     else:
            #         V[k] = tmp[j]
            #         j += 1

def merge_sort_v2(V, a=0, b=None):
    if type(V) != list:
        print("errore, non hai passato una lista")
        return None
    if b == None:
        b = len(V) - 1

    if b > a:
        if b-a < 2:
            if V[a] > V[b]:
                V[a], V[b] = V[b], V[a]
        else:
            mid = (a + b) // 2
            merge_sort_v2(V, a, mid)
            merge_sort_v2(V, mid+1, b)

            # merge
            # i = a
            # j = mid+1
            # tmp = []
            # for _ in range(b-a+1):
            #     if i > mid:
            #         tmp.append(V[j])
            #         j += 1
            #     elif j > b:
            #         tmp.append(V[i])
            #         i += 1
            #     elif V[i] <= V[j]:
            #         tmp.append(V[i])
            #         i += 1
            #     else:
            #         tmp.append(V[j])
            #         j += 1

            # for i in range(len(tmp)):
            #     V[a+i] = tmp[i]

            tmp = V[a: b+1]
            i = 0
            j = mid-a+1
            for k in range(a, b+1):
                if i > mid-a:
                    V[k] = tmp[j]
                    j += 1
                elif j > b-a:
                    V[k] = tmp[i]
                    i += 1
                elif tmp[i] <= tmp[j]:
                    V[k] = tmp[i]
                    i += 1
                else:
                    V[k] = tmp[j]
                    j += 1


# V = [14, 8, 3, 10, 2, 5, 6, 21]
# V = [random.randint(0, 10) for _ in range(10)]
# print(V)
# merge_sort_v1(V)
# print(V)
# V = [random.randint(0, 10) for _ in range(10)]
# print(V)
# merge_sort_v1(V)
# print(V)
