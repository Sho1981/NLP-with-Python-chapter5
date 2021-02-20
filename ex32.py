import nltk
from nltk.corpus import brown
from collections import defaultdict

brown_tagged_sents = brown.tagged_sents(categories='news')

dict = defaultdict(lambda: defaultdict(set))
for i in range(len(brown_tagged_sents)):
    for (w1,t1), (w2,t2) in nltk.bigrams(brown_tagged_sents[i]):
        dict[w1][t1].add(t2) 

print(dict['the'])
