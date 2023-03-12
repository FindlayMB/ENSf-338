import matplotlib.pyplot as plt
from timeit import timeit
from random import randint, seed


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
        mid = start + (end - start) // 2
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
    seed(1)
    for i in range(100):
        linearTime.append(
            timeit(lambda: linearSearch(data, randint(1, 1500)), number=1))
        binaryTime.append(
            timeit(lambda: binarySearch(data, randint(1, 1500)), number=1))

    plt.hist(linearTime, label="Linear Search Time")
    plt.hist(binaryTime, label="Binary Search Time")
    plt.show()
