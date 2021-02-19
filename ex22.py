# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'.*self$', 'PPLS'),
    (r'.*seles$', 'PPLS'),
    (r'^some.*', 'PN'),
    (r'^any.*', 'PN'),
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'.*', 'NN'),
]

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
regexp_tagger = nltk.RegexpTagger(patterns)
print(regexp_tagger.evaluate(brown_tagged_sents))
