'''
https://en.wikipedia.org/wiki/Radix_sort
'''
import numpy as np

def writeData(array,seedNum):
    # Writes the array to a csv file named dataS<seed number>Sorted.csv
    with open(f'dataS{seedNum}Sorted.csv','w') as outFile:
        for x in range(10):
            for y in range(9):
                outFile.write(str(array[x,y])+',')
            outFile.write(f'{str(array[x,9])}\n')

def readData(seedNum):
    '''
        Returns the array read from the csv file named dataS<seed number>.csv
    '''
    array = np.genfromtxt(f'dataS{seedNum}.csv',delimiter=',',dtype=int)
    print(array)
    return array

def radixSort(array):
    pass

def main():
    seedNum = 1 # Data set selected, is the same as the seed number

    # Reads the array from the csv file named dataS<seed number>.csv
    array = readData(seedNum) 
    writeData(array,seedNum)

if __name__ == "__main__":
    main()

