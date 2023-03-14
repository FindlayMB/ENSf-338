import matplotlib.pyplot as plt
from timeit import timeit
import random
import numpy as np
import statistics


def linearSearch(data, x):
    # Inefficient search for a sorted array
    for index, value in enumerate(data):
        if value == x:
            return index
    return -1


def binarySearch(data, value):
    # Efficient search for a sorted array
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (end + start) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == "__main__":
    data = list(range(1, 1501))
    linearTime = []
    binaryTime = []
    random.seed(a=1)
    # Run the search functions 100 times each and append the execution times to their respective lists
    for i in range(100):
        x = random.randint(1, len(data))
        linearTime.append(timeit(lambda: linearSearch(data, x), number=1))
        binaryTime.append(timeit(lambda: binarySearch(data, x), number=1))

    # Print the minimum and average execution times for both search functions
    print("Linear Search:")
    print(f"Minimum time: {min(linearTime):.6f}s")
    print(f"Average time: {statistics.mean(linearTime):.6f}s")

    print("\nBinary Search:")
    print(f"Minimum time: {min(binaryTime):.6f}s")
    print(f"Average time: {statistics.mean(binaryTime):.6f}s")

    # Plot the distributions of measured values
    plt.hist(linearTime, alpha=0.5, label='Linear Search')
    plt.hist(binaryTime, alpha=0.5, label='Binary Search')
    plt.legend(loc='upper right')
    plt.xlabel('Execution Time (s)')
    plt.ylabel('Frequency')
    plt.show()
