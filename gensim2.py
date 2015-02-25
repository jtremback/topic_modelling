from gensim import corpora, models, similarities, utils
import json
import re


# collect statistics about all tokens
dictionary = corpora.Dictionary(
  re.sub(r'[^\w|\ ]|_|\d', '', line).lower().split()
  for line in open('few_documents')
)

# filter out extremes
dictionary.filter_extremes(2, .01)

# stoplist = set('for a of the and to in'.split())

# # remove stop words and words that appear only once
# stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
#             if stopword in dictionary.token2id]

# once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
# dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
# dictionary.compactify() # remove gaps in id sequence after words that were removed
dictionary.save('dict')
dictionary.save_as_text('dict.txt')
print(dictionary)


# class MyCorpus(object):
#   def __iter__(self):
#     for line in open('documents'):
#       # assume there's one document per line, tokens separated by whitespace
#       yield dictionary.doc2bow(line.lower().split())

# corpus_memory_friendly = MyCorpus()

# # for vector in corpus_memory_friendly: # load one vector into memory at a time
# #   print(vector)

# corpora.MmCorpus.serialize('mmcorpus', corpus_memory_friendly)