import sys
import json
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = p = array[(start+end)//2]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


with open("ex2.json", "r") as file:
    inputs = json.load(file)

timing_results = []

for i, arr in enumerate(inputs):
    start_time = time.perf_counter()
    func1(arr, 0, len(arr) - 1)
    end_time = time.perf_counter()
    timing_results.append(end_time - start_time)
    
with open("ex2.5.json", "w") as f:
    f.write(str(inputs))

plt.plot(timing_results)
plt.xlabel("Input")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Timing Results")
plt.show()
