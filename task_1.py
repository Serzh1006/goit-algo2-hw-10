import random
import time
import statistics


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


def measure_sort_time(sort_func, arr, repeats=5):
    times = []
    for _ in range(repeats):
        copy_arr = arr.copy()
        start = time.perf_counter()
        sort_func(copy_arr)
        end = time.perf_counter()
        times.append(end - start)
    return statistics.mean(times)


sizes = [10_000, 50_000, 100_000, 500_000]

for size in sizes:
    test_array = [random.randint(0, 1_000_000) for _ in range(size)]
    rand_time = measure_sort_time(randomized_quick_sort, test_array)
    det_time = measure_sort_time(deterministic_quick_sort, test_array)

    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд\n")
