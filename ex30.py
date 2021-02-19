# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown

def bitagger_train(train_sents, backoff=False):
    if backoff == True:
        t0 = nltk.DefaultTagger('NN')
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
    else:
        t2 = nltk.BigramTagger(train_sents)
    return t2

def lfwords_unk(tagged_sent, hf_words):
    unk_sent = []
    for word, tag in tagged_sent:
        if word in hf_words:
            unk_sent.append((word, tag))
        else:
            unk_sent.append(('UNK', tag))
    return unk_sent

brown_tagged_sents = brown.tagged_sents(categories='news')
sents_size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:sents_size]
test_sents = brown_tagged_sents[sents_size:]
words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
hfwords_size = 1000

train_sents = [lfwords_unk(tagged_sent, words_by_freq[:hfwords_size])
                                    for tagged_sent in train_sents]

t2 = bitagger_train(train_sents, backoff = True)
print(t2.evaluate(test_sents))

t2 = bitagger_train(train_sents, backoff = False)
print(t2.evaluate(test_sents))
