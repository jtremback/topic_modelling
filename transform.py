import logging
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

dictionary = corpora.Dictionary.load('data/tiny.dict')
corpus = corpora.MmCorpus('data/tiny.mm')
# print(corpus)

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]
# for doc in corpus_tfidf:
#     print(doc)

# initialize an LSI transformation
lsi = models.LsiModel(corpus, id2word=dictionary)
# create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
corpus_lsi = lsi[corpus_tfidf]

# lsi.print_topics()


doc = "Human computer interaction"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]  # convert the query to LSI space

index = similarities.MatrixSimilarity(lsi[corpus])

# perform a similarity query against the corpus
sims = index[vec_lsi]

sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(sims)
