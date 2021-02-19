# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown

def search_comback_index(bigram_tagged_words):
    before_tag = 'NN'
    for i, taggedword in enumerate(bigram_tagged_words):
        if taggedword[1] != 'None' and before_tag == 'None':
            return i
        before_tag = taggedword[1]
    return -1

def search_comback(sent, bigram_tagger):
    btw = bigram_tagger.tag(sent)
    print(btw)
    btw = [('word', 'PP'), ('word', 'PP'), ('word', 'None'), ('word', 'None'), 
            ('word', 'None'), ('word', 'None'), ('word', 'PP'), ('word', 'PP'), ]
    print(btw)
    i = search_comback_index(btw)
    if i != -1:
        print('sentence:', btw[i-1:i+3])

#init
brown_tagged_sents = brown.tagged_sents(categories = 'news')
brown_sents = brown.sents(categories = 'news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
bigram_tagger = nltk.BigramTagger(train_sents)

for cat in brown.categories():
    print('categories =', cat)
    brown_words = brown.words(categories = cat)
    search_comback(brown_words, bigram_tagger)
