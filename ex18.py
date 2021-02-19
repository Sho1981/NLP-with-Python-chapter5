# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown

def percent(word, cfd):
    tag_freq = sorted([cfd[word][tag] for tag in list(cfd[word])], reverse=True)
    return tag_freq[0] / sum(tag_freq)

cfd = nltk.ConditionalFreqDist([(w, t)
                        for (w, t) in brown.tagged_words(categories='news')])

#Ex18(a)
print()
print('ex.18.a. percentage of words tagged only tag')
percents = {w: percent(w, cfd) for w in set(brown.words(categories='news'))}
onlytag_word_percent = len([w for w,p in percents.items() if p == 1.0])\
                                                            / len(percents)
print('%.2f%%' % (100*onlytag_word_percent))

#Ex18(b)
print()
print('ex.18.b. percentage of words tagged 2 or more tags')
print('%.2f%%' % (100.0 - 100*onlytag_word_percent))

#Ex18(c)
print()
print('ex.18.c. percentage of words tagged only tag in brown corpus')
bw = brown.words(categories='news')
print('%.2f%%' % (100*len([w for w in bw if percents[w]==1.0]) / len(bw)))

