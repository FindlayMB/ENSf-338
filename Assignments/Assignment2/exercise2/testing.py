import sys
import json
import timeit
import numpy as np

import sys
'''
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low >= high or low < 0 or high < 0:
        return
    pi = func2(arr, low, high)
    func1(arr, low, pi)
    func1(arr, pi + 1, high)

def func2(array, start, end):
    mid = (start+end)//2
    p = array[mid]
    low = start - 1
    high = end + 1
    while True:
        low = low + 1
        while array[low] < p:
            low = low + 1
        high = high - 1
        while array[high] > p:
            high = high - 1
        if low >= high:
            return high
        array[low], array[high] = array[high], array[low]
        '''
def func1(arr, low, high):
    if high - low <= 15:
        insertion_sort(arr, low, high)
        return
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi - 1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    median = median_of_three(array, start, end)
    pivot = array[median]
    array[median], array[start] = array[start], array[median]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def median_of_three(array, start, end):
    mid = (start + end) // 2
    if array[start] > array[mid]:
        array[start], array[mid] = array[mid], array[start]
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
    if array[mid] > array[end]:
        array[mid], array[end] = array[end], array[mid]
    return mid

def insertion_sort(array, start, end):
    for i in range(start + 1, end + 1):
        key = array[i]
        j = i - 1
        while j >= start and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


def sortQ(array, low, high):
    if low >= high:
        return
    pivot = partition(array,low, high)
    sortQ(array, low, pivot-1)
    sortQ(array, pivot+1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= pivot:
            i= i + 1
            (array[i],array[j]) = (array[j],array[i])

    (array[i+1],array[high]) = (array[high],array[i+1])
    
    return (i+1)


def main(): 
    with open('ex2.json','r') as iF:
        array = json.load(iF)
    arrays = []
    for arr in array:
        func1(arr,0,len(arr)-1)
        arrays.append(arr)
    

# write data to a new json file 
    with open("ex2.5.json", "w") as outfile:
        outfile.write(json.dumps(arrays))
'''  
    num_elements = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]


    plt.xticks(num_elements)
    
    plt.plot(num_elements, times, label = "original algorithm")
    plt.title("Quicksort Algorithm Timing VS Number of Array Elements")
    
    plt.ylabel("Time it Takes to Sort (Seconds)")
    plt.xlabel("Number of Array Elements")
    plt.legend()
    plt.show()
'''

if __name__ == "__main__":
    main()