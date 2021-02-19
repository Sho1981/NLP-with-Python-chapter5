# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown

def percent(word, cfd):
    tag_freq = sorted([cfd[word][tag] for tag in list(cfd[word])], reverse=True)
    return tag_freq[0] / sum(tag_freq)

cfd = nltk.ConditionalFreqDist([(w, t)
                        for (w, t) in brown.tagged_words(categories='news')])

percents = [percent(w, cfd) for w in set(brown.words(categories='news'))]
print(sum(percents) / len(percents))
