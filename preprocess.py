from gensim import corpora, models, similarities, utils
import json
import re

def process_line(line):
  # regex out punctuation etc, lowercase, split on space, filter out strings
  # with length < 2
  return filter(lambda x: len(x) > 1, re.sub(r'[^\w|\ ]|_|\d', '', line).lower().split())

# collect statistics about all tokens
dictionary = corpora.Dictionary(process_line(line) for line in open('data/few_documents'))

# filter out extremes
dictionary.filter_extremes(2, .01)

dictionary.save('data/dict')
dictionary.save_as_text('data/dict.txt')
print(dictionary)

class MyCorpus(object):
  def __iter__(self):
    for line in open('data/documents'):
      # assume there's one document per line, tokens separated by whitespace
      yield dictionary.doc2bow(process_line(line))

corpora.MmCorpus.serialize('data/mmcorpus', MyCorpus())