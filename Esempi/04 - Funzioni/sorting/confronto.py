import time
import random
import bubble_sort as bs
import selection_sort as ss
import quick_sort as qs
import merge_sort as ms

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

nripetizioni = 10000

nalgoritmi = 5
tempi = [0 for _ in range(nalgoritmi)]

for esp in range(1, 20):
    n = 2**esp

    print("Con array di cardinalità", n)

    # bubble sort
    if (tempi[0] < 1):
        V = [random.randint(0, 100) for _ in range(n)]
        start_time = time.time()
        bs.bubble_sort(V)
        total_time = time.time() - start_time
        tempi[0] = total_time
        print(f"Bubble Sort   : {total_time:.5f}")
    else:
        print(f"Bubble Sort   : non calcolato")
        

    # selection sort
    if (tempi[1] < 1):
        V = [random.randint(0, 100) for _ in range(n)]
        start_time = time.time()
        ss.selection_sort(V)
        total_time = time.time() - start_time
        tempi[1] = total_time
        print(f"Selection Sort: {total_time:.5f}")
    else:
        print(f"Selection Sort: non calcolato")

    # quick sort
    if (tempi[2] < 1):
        V = [random.randint(0, 100) for _ in range(n)]
        start_time = time.time()
        qs.quick_sort(V)
        total_time = time.time() - start_time
        tempi[2] = total_time
        print(f"Quick Sort    : {total_time:.5f}")
    else:
        print(f"Quick Sort    : non calcolato")
    
    # merge sort 1
    if (tempi[3] < 1):
        V = [random.randint(0, 100) for _ in range(n)]
        start_time = time.time()
        ms.merge_sort_v1(V)
        total_time = time.time() - start_time
        tempi[3] = total_time
        print(f"Merge Sort 1  : {total_time:.5f}")
    else:
        print(f"Merge Sort 1  : non calcolato")
    
    # merge sort 2
    if (tempi[4] < 1):
        V = [random.randint(0, 100) for _ in range(n)]
        start_time = time.time()
        ms.merge_sort_v2(V)
        total_time = time.time() - start_time
        tempi[4] = total_time
        print(f"Merge Sort 2  : {total_time:.5f}")
    else:
        print(f"Merge Sort 2  : non calcolato")

    print()



# start_time = time.time()

# print("Classico: %s seconds ---" % (time.time() - start_time))
    
    
# V = [random.randint(0, 100) for _ in range(5)]
# A = V.copy()
# A[0] = -1
# print(V)
# print(A)