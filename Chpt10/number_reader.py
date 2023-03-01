import json

fileName='numbers.json'
with open(fileName) as f:
    numbers= json.load(f)

print(numbers)