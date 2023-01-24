import sys

def checkPrime():
  try:
    number = int(float(sys.argv[1]))
  except:
    print("INVALID INPUT!")
    return
  if number < 2:
    print('No')
  else:
    for i in range(2, number):
      if number % i == 0:
        print('No')
        return
    print('Yes')

checkPrime()