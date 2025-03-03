import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr[:])  # Use a copy to avoid modifying the original array
    return time.time() - start_time

# Test sorting times for different input sizes
sizes = [100, 200, 500, 1000, 2000, 5000]
bubble_times = []
selection_times = []
insertion_times = []

for size in sizes:
    random_list = [random.randint(0, 10000) for _ in range(size)]
    bubble_times.append(measure_time(bubble_sort, random_list))
    selection_times.append(measure_time(selection_sort, random_list))
    insertion_times.append(measure_time(insertion_sort, random_list))

# Plot the time analysis for varying input sizes
plt.plot(sizes, bubble_times, marker='o', label="Bubble Sort", color='blue')
plt.plot(sizes, selection_times, marker='s', label="Selection Sort", color='green')
plt.plot(sizes, insertion_times, marker='^', label="Insertion Sort", color='red')
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Performance vs Input Size")
plt.legend()
plt.grid()
plt.show()
plt.savefig("sprt.png")