import numpy as np
from numpy.random import seed, randint

def genRandomArray():
    numbers = randint(low=1,high=101,size=(10,10))
    print(numbers)
    return numbers

def writeData(array,seedNum):
    with open(f'dataS{seedNum}.csv','w') as outFile:
        for x in range(10):
            for y in range(9):
                outFile.write(str(array[x,y])+',')
            outFile.write(f'{str(array[x,9])}\n')
    
def readData(seedNum):
    '''
        Reads the array from the csv file named dataS<seed number>.csv
    '''
    array = np.genfromtxt(f'dataS{seedNum}.csv',delimiter=',',dtype=int)
    print(array)

def main():
    # Seed number, change for a different array
    seedNum = 1 
    seed(seedNum)

    # Generates a 10x10 array filled with randomnumbers from 1-100
    array = genRandomArray() 

    # Writes the array to a csv file named dataS<seed number>.csv
    writeData(array,seedNum)

    # Reads the array from the csv file named dataS<seed number>.csv
    readData(seedNum)

if __name__ == "__main__":
    main()