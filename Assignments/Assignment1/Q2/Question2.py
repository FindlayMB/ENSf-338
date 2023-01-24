import json

with open("data.json", "r") as inFile:
    content = json.load(inFile)
inFile.close()

reversedContent = [content[i] for i in range(len(content)-1,-1,-1)]

with open("reverse_data.json","w") as outFile:
    outFile.write(json.dumps(reversedContent, indent = 4))
outFile.close()