# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown
import re
from collections import defaultdict

def plural(word, tagdict):
    """Return plural noun of word"""
    plural_cand = [word+'s',                    #ex)apples
                   word+'es',                   #ex)glasses
                   word[:(len(word)-1)]+'ies',  #ex)candies
                   word[:(len(word)-1)]+'ves']  #ex)wolves

    return [plural_cand[i] for i, w in enumerate(plural_cand)
                           if 'NNS' in tagdict[w]]

def sum_tag_words_freq(words, tag, cfd):
    """Return total amount of tagged words frequency"""
    return sum(cfd[w][tag] for w in words)

cat = 'news'

brown_tagged_words = brown.tagged_words(categories=cat)
brown_words_tagdict = defaultdict(lambda: [])
for w,tag in set(brown_tagged_words):
    brown_words_tagdict[w].append(tag)
cfd = nltk.ConditionalFreqDist((w, tag) for w in brown.words(categories=cat)
                                        for tag in brown_words_tagdict[w])

#Ex15(a)
print()
print('ex.15.a. words plural is appeared more than singular.')
more_plural_words =\
    [w for w,_ in set(brown_tagged_words)
     if sum_tag_words_freq([w], 'NN', cfd)
      < sum_tag_words_freq(plural(w, brown_words_tagdict), 'NNS', cfd)]
print(more_plural_words[:20], '...')
print('number of words \'plural > singular\' is', len(more_plural_words))

#Ex15(b)
print()
print('ex.15.b. most tagged words')
most_tagnum = max(len(tags) for tags in brown_words_tagdict.values())
most_tagged_words = [(word, tags) for word, tags
                                  in brown_words_tagdict.items()
                                  if len(tags) == most_tagnum]
print(most_tagged_words)

#Ex15(c)
print()
print('ex.15.c. 20 tags appeared most freguently')
fd = nltk.FreqDist(tag for _,tag in brown_tagged_words)
print(sorted([(fd[tag], tag) for tag in fd], reverse=True)[:20])

#Ex15(d)
print()
print('ex.15.d. most frequent tag before noun')
bigram_tags = [(brown_tagged_words[i][1], brown_tagged_words[i+1][1])
                for i in range(len(brown_tagged_words)-1)]
fd = nltk.FreqDist([t1 for t1, t2 in bigram_tags if t2.startswith('NN')])
mft = sorted([(fd[tag], tag) for tag in fd], reverse=True)
print('Most frequense tag before noun is',\
        mft[0][1], '('+str(mft[0][0])+'times)')
print('word is', [w for (w,tags) 
                    in brown_words_tagdict.items() if 'AT' in tags])
