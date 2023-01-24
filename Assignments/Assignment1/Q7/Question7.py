
import timeit

def pow2ForLoop(n):
    powers = []
    for i in range(n): 
        powers.append(2**i)
    return powers

def pow2ListComp(n):
    return [2**i for i in range(n)]

def pow2(n):
    return 2**n

elapsedTime = timeit.timeit(lambda: pow2(10000),number=10000)
elapsedTimeFL = timeit.timeit(lambda: pow2ForLoop(1000),number=1000)
elapsedTimeLC = timeit.timeit(lambda: pow2ListComp(1000),number=1000)
print(f'Time for 10000 powers of 2 is {elapsedTime}')
print(f'For loop:\tTime for 1000 powers of 2 is {elapsedTimeFL}')
print(f'List Comp:\tTime for 1000 powers of 2 is {elapsedTimeLC}')