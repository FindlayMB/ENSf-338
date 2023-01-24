from time import perf_counter

timeStart = perf_counter()

writeFile = open('write.txt','a',encoding='utf-8')
readFile = open('read.txt','r',encoding='utf-8')
writeFile.write(readFile.read().upper())

timeStop = perf_counter()

print(f'Time: {timeStop-timeStart}')