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
    unsorted = [38,13,73,10,76,6,80,65,17,2]
    sortQ(unsorted,0,len(unsorted)-1)
    print(unsorted)

if __name__=="__main__":
    main()