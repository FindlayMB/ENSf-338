import matplotlib.pyplot as plt
from timeit import timeit
import random


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
    data = list(range(1500))
    linearTime = []
    binaryTime = []
