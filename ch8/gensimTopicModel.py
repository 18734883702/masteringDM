# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:38:13 2016

@author: megan squire
"""
from gensim import corpora
from gensim.models.ldamodel import LdaModel
from gensim.parsing.preprocessing import STOPWORDS

num_topics = 4
num_words = 5
passes = 20

# sample files for testing
# in each file, one line = one "document"
filename = 'data/introSectionsToChapters.txt'
# filename = 'data/sampleTextFromCh7.txt'
# filename = 'data/gnueIRCsummary.txt'
# filename = 'data/apacheMeetingMinutes.txt'
# filename = 'data/lkmlEmailsReduced.txt'
# filename = 'data/lkmlLinusJan2006.txt'

with open(filename, encoding='utf-8') as f:
    documents = f.readlines()

# each document is turned into a list of words
# the words are lowercased, then stopwords and contractions removed
# this bit is close to the structure used in the Gensim tutorial, where
# you can also get more info on Gensim & how it works: 
# https://radimrehurek.com/gensim/tut1.html
texts = [[word for word in document.lower().split()
#         if word not in STOPWORDS and word.isalnum() and word is not 'linus']
         if word not in STOPWORDS and word.isalnum()]
         for document in documents]

# create dictionary from the list of word lists
dictionary = corpora.Dictionary(texts)
print(dictionary)

# the corpus is a list of vectors, one per document
corpus = [dictionary.doc2bow(text) for text in texts]

# create LDA model: values for topics & passes can be adjusted
# a higher number of passes takes longer but is more accurate
lda = LdaModel(corpus,
               id2word=dictionary,
               num_topics=num_topics,
               passes=passes)

# improved printing from what was originally in Ch 8
for topic in lda.print_topics(num_words = num_words):
    termNumber = topic[0]
    print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    for term in listOfTerms:
        listItems = term.split('*')
        print('  ', listItems[1], '(', listItems[0], ')', sep='')
