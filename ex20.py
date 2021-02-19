# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown

def searchbrown_word(tag):
    """
    Search word in brown corpus by input tags.
    return list
    tag: str
    """
    brown_tagged_words = brown.tagged_words(categories='news')
    hitwords = []
    for i in range(len(brown_tagged_words)):
        if tag == brown_tagged_words[i][1]:
            hitwords.append(brown_tagged_words[i][0].lower())
    return hitwords

def searchbrown_phrase(tags):
    """
    Search phrase in brown corpus by input tags.
    return touple
    tags: list ([tag, tag, ...])
    """
    l = len(tags)
    brown_tagged_words = brown.tagged_words(categories='news')
    hitwords = []
    for i in range(len(brown_tagged_words)-l+1):
        searchtags = [tag for _,tag in brown_tagged_words[i:i+l]]
        if tags == searchtags:
            hitwords.append(tuple([w.lower()
                            for w,_ in brown_tagged_words[i:i+l]]))
    return hitwords

#Ex20(a)
print()
print('ex.20.a. search difference words tagged \'MD\' and sort to list')
print(sorted([w for w in set(searchbrown_word('MD'))]))

#Ex20(b)
print()
print('ex.20.b. search difference words tagged \'MD\' and sort to list')
print('NNS\n', sorted([w for w in set(searchbrown_word('NNS'))]))
print('VBZ\n', sorted([w for w in set(searchbrown_word('VBZ'))]))

#Ex20(c)
print()
print('ex.20.c. search phrase tagged \'IN+DET+NN\'')
print('IN+AT+NN\n', sorted([w for w in set(searchbrown_phrase(['IN', 'AT', 'NN']))]))
print('IN+DTI+NN\n', sorted([w for w in set(searchbrown_phrase(['IN', 'DTI', 'NN']))]))
print('IN+AP+NN\n', sorted([w for w in set(searchbrown_phrase(['IN', 'AP', 'NN']))]))

#Ex20(d)
print()
print('ex.20.d. ratio of male pronoun to female pronoun')
pp_list = searchbrown_word('PPS') + searchbrown_word('PPO')\
 + searchbrown_word('PP$') + searchbrown_word('PP$$') + searchbrown_word('PPL')
num_mpp = sum(1 for w in pp_list if w in ['he', 'his', 'him', 'himself'])
num_fpp = sum(1 for w in pp_list if w in ['she', 'her', 'hers', 'herself'])

print('male pronoun: %.2f%%, female pronoun: %.2f%%'
                            % (num_mpp / (num_mpp + num_fpp) * 100,
                               num_fpp / (num_mpp + num_fpp) * 100))
