import json 

number=[2,3,5,7,11,13]

fileName= 'numbers.json'
with open(fileName, 'w') as f:
    json.dump(number, f)