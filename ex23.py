# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

size = int(len(brown_tagged_sents)*0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

print('Ngram Tagger Ecaluate Score')
print('    train_sents test_sents')

for i in range(1,7):
    ngram_tagger = nltk.NgramTagger(i, train_sents)
    print('i=%d      %.4f     %.4f' % (i, ngram_tagger.evaluate(train_sents), 
                                   ngram_tagger.evaluate(test_sents)))
