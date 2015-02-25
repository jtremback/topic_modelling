from __future__ import print_function
import json
import leveldb

db = leveldb.LevelDB('./db')
subset = open('subset')
documents = open('documents', 'w')

# count = 0

# for line in iter(log):
#   json_line = json.loads(line)

#   if 'terms' in json_line['val']:
#     count += 1
#     if count % 1000 == 0:
#       print(count)

#     db.Put(str(json_line['key']), json.dumps(json_line['val']))


# count = 0

# for doc in db.RangeIter():
#   count += 1
#   if count % 1000 == 0:
#     print(count)
#   if count == 10000:
#     break
#   subset.write(doc[1] + '\n')


# count = 0

# for doc in db.RangeIter():
#   json_val = json.loads(doc[1])

#   count += 1
#   if count % 1000 == 0:
#     print(count)
#   if count == 10000:
#     break

#   if json_val['lang_terms'] == 'en':
#     for term in json_val['terms']:

#       documents.write(term['definition'].encode('utf8') + ' ' + term['term'].encode('utf8') + '\n')

# count = 0

# for line in iter(subset):
#   count += 1
#   print(count)

#   json_line = json.loads(line)

#   for term in json_line['terms']:
#     documents.write(term['definition'].encode('utf8') + ' ' + term['term'].encode('utf8') + '\n

