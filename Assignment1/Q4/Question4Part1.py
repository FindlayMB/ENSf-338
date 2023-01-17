import json

with open("vehicles.json", "r") as inFile:
    content = json.load(inFile)

for id,entry in enumerate(content):
    entry['id'] = id

with open("data.json","w") as outFile:
    outFile.write(json.dumps(content, indent = 4))