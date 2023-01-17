from time import perf_counter

timeStart = perf_counter()
writeFile = open('write.txt','a',encoding='utf-8')
readFile = open('read.txt','r',encoding='utf-8')

for i in readFile.read().upper():
    writeFile.write(i)

timeStop = perf_counter()

print(f'Time: {timeStop-timeStart}')