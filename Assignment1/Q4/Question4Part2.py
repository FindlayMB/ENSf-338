import json

"""
    Please run this code after running the first part of the question.
"""

with open("data.json", "r") as inFile:
    content = json.load(inFile)

count = 0
average = 0
for entry in content:
    if entry['speed'] > 5:
        count += 1
        average += entry['speed']

print(count)
print(average)
average /= count
print(average)