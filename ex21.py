# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown

def before(word, before_tag, tagged_bigrams):
    return [tagged_bigrams[i][0] for i in range(len(tagged_bigrams))
                            if tagged_bigrams[i][1][0] == word
                            and tagged_bigrams[i][0][1] == before_tag]

cat = 'romance'
brown_tagged_words = brown.tagged_words(categories=cat)
tagged_bigrams = [(brown_tagged_words[i], brown_tagged_words[i+1])
                for i in range(len(brown_tagged_words)-1)]

print(before('adore', 'QL', tagged_bigrams))
print(before('adored', 'QL', tagged_bigrams))
print(before('love', 'QL', tagged_bigrams))
print(before('loved', 'QL', tagged_bigrams))
print(before('like', 'QL', tagged_bigrams))
print(before('liked', 'QL', tagged_bigrams))
print(before('prefer', 'QL', tagged_bigrams))
print(before('prefered', 'QL', tagged_bigrams))
#print(before('too', 'QL', tagged_bigrams))
#print(before('pure', 'QL', tagged_bigrams))
#print(before('frantic', 'QL', tagged_bigrams))
#print(before('hard', 'QL', tagged_bigrams))
