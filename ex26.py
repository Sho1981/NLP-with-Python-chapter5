# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown

def performance(train_sents, test_sents):
    unigram_tagger = nltk.UnigramTagger(train_sents)
    return unigram_tagger.evaluate(test_sents)

def display():
    import pylab
    brown_tagged_sents = brown.tagged_sents(categories='news')
    test_sents = brown.tagged_sents(categories='editorial')
    sizes = [int(len(brown_tagged_sents)*rate)
                                     for rate in 0.1*pylab.arange(1, 11)]
    perfs = [performance(brown_tagged_sents[:size],
                         test_sents)
                         for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

display()

