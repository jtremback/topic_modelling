from gensim import corpora
import re
import sys
import json
import leveldb

source = sys.argv[1]
name = sys.argv[2]
limit = int(sys.argv[3])

db = leveldb.LevelDB(source)

import logging
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO
)


def normalize(line):
    # regex out punctuation etc, lowercase, split on space, filter out strings
    # with length < 2
    return filter(
        lambda x: len(x) > 1, re.sub(r'[^\w|\ ]|_|\d', '', line)
        .lower().split()
    )


# a generator that yields docs formatted for gensim: <term> <definition>
def yield_docs(db, limit):
    count = 0
    for record in db.RangeIter():
        # stop if limit is reached, if limit exists
        count = count + 1
        if limit:
            print(count, limit)
            if count == limit:
                break

        json_record = json.loads(record[1])

        for term in json_record['terms']:
            yield term['definition'].encode('utf8') + ' ' + (
                term['term'].encode('utf8') + '\n')


def make_dictionary(db, limit):
    # init dictionary
    dictionary = corpora.Dictionary()

    # collect statistics about all tokens
    for doc in yield_docs(db, limit):
        # print(normalize(doc))
        # add document to dictionary
        dictionary.doc2bow(normalize(doc), allow_update=True)

    return dictionary


def yield_corpus(dictionary, db, limit):
    for doc in yield_docs(db, limit):
        yield dictionary.doc2bow(normalize(doc))


dictionary = make_dictionary(db, limit)
dictionary.filter_extremes(2, .01)
dictionary.save('data/' + name + '.dict')
dictionary.save_as_text('data/' + name + '.txt')


corpora.MmCorpus.serialize(
    'data/' + name + '.mm',
    yield_corpus(dictionary, db, limit)
)
