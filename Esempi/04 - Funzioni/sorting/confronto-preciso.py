import time
import random
import bubble_sort as bs
import selection_sort as ss
import quick_sort as qs
import merge_sort as ms
nripetizioni = 10000

for esp in range(1, 5):
    n = 10**esp

    print("Con array di cardinalità", n)

    # bubble sort
    V = [random.randint(0, 100) for _ in range(n)]
    start_time = time.time_ns()
    bs.bubble_sort(V)
    total_time = time.time_ns() - start_time
    print(f"Bubble Sort   : {total_time}")

    # selection sort
    V = [random.randint(0, 100) for _ in range(n)]
    start_time = time.time_ns()
    ss.selection_sort(V)
    total_time = time.time_ns() - start_time
    print(f"Selection Sort: {total_time}")

    # quick sort
    V = [random.randint(0, 100) for _ in range(n)]
    start_time = time.time_ns()
    qs.quick_sort(V)
    total_time = time.time_ns() - start_time
    print(f"Quick Sort    : {total_time}")

    # merge sort 1
    V = [random.randint(0, 100) for _ in range(n)]
    start_time = time.time_ns()
    ms.merge_sort_v1(V)
    total_time = time.time_ns() - start_time
    print(f"Merge Sort 1  : {total_time}")

    # merge sort 1
    V = [random.randint(0, 100) for _ in range(n)]
    start_time = time.time_ns()
    ms.merge_sort_v2(V)
    total_time = time.time_ns() - start_time
    print(f"Merge Sort 2  : {total_time}")

    print()



# start_time = time.time()

# print("Classico: %s seconds ---" % (time.time() - start_time))
    
    
# V = [random.randint(0, 100) for _ in range(5)]
# A = V.copy()
# A[0] = -1
# print(V)
# print(A)