import json
import matplotlib.pyplot as plt

with open("golddata.json","r") as inFile:
    content = json.load(inFile)

usdData = []
zarData = []
dates = []
for entry in content:
    if entry['Date'][6:] == '2010':
        usdData.append(entry['United States(USD)'])
        zarData.append(entry['South Africa(ZAR)'])
        dates.append(entry['Date'])
plt.figure('US')
plt.bar(x = range(len(dates)), height = usdData, tick_label = dates)
plt.title('Price of gold in 2010 for United States')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.figure('SA')
plt.bar(x = range(len(dates)), height = zarData, tick_label = dates)
plt.title('Price of gold in 2010 for South Africa')
plt.xlabel('Date')
plt.ylabel('Price (ZAR)')
plt.show()