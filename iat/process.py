import json


with open('results.json', 'r') as f:
    results = json.loads(f.read())

for result in results:
    print result
