import sys

def checkPrime():
  number = int(sys.argv[1])
  if number < 2:
    print('No')
  else:
    for i in range(2, number):
      if number % i == 0:
        print('No')
        return
    print('Yes')

checkPrime()