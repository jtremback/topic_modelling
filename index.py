import json

f = open('db')

for line in iter(f):
    line = json.loads(line)
    terms = line['val']

f.close()