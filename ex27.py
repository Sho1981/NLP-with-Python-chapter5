# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown
import re

def generate_test_tags():
    brown_tagged_sents = brown.tagged_sents(categories='news')
    size = int(len(brown_tagged_sents)*0.9)
    train_sents = brown_tagged_sents[:size]
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    return [tag for sent in brown.sents(categories='editorial')
                for (word, tag) in t2.tag(sent)]

def generate_gold_tags():
    return [tag for (word, tag) in brown.tagged_words(categories='editorial')]

"""
#unused
def print_cmat_values(cm, tag_list):
    for gold_tag in tag_list:
        print('%15s: ' % gold_tag, end = '')
        for test_tag in tag_list:
            if cm[gold_tag, test_tag]:
                print('%s=%d, ' % (test_tag, cm[gold_tag, test_tag]), end = '')
        print()

def print_cmat_values2(cm, tag_list):
    for tag in tag_list:
        gold_to_test = [test_tag for test_tag in tag_list if cm[tag, test_tag]]
        test_to_gold = [gold_tag for gold_tag in tag_list if cm[gold_tag, tag]]

        #ignore tag, gold=test=tag or 3 or more tags
        if gold_to_test == [tag] and test_to_gold == [tag]:
            continue
        elif len(gold_to_test) > 2 or len(test_to_gold) > 2:
            continue
        else:
            print("'%s':" % tag, end = '')
            print(gold_to_test)
            print("'%s': " % tag, end = '')
            print(test_to_gold)
        print()
"""

test_tags = generate_test_tags()
gold_tags = generate_gold_tags()
print('      test tagger accuracy : %.4f' % nltk.accuracy(gold_tags, test_tags))

#make confusion matrix
cm = nltk.ConfusionMatrix(gold_tags,test_tags)
tag_list = [w.split()[1] for w in re.findall(r'[0-9]+.*\n', cm.key())]

#make simple tag dict.
marge = {'*-HL':'*', ',-HL':',', '---HL':'--', '.-HL':'.', ':-HL':':',
         ':-TL':':', 'ABN-TL':'ABN', 'AP-TL':'AP', 'AT-HL':'AT', 'BE-HL':'BE',
         'BER-HL':'BER', 'BER-TL':'BER', 'BEZ-HL':'BEZ', 'BEZ-TL':'BEZ',
         'CC-HL':'CC', 'CC-TL':'CC', 'CD-HL':'CD', 'DO-HL':'DO', 'DO-TL':'DO',
         'DOZ-HL':'DOZ', 'HVN':'HVD', 'IN-NC':'IN', 'JJ-TL-HL':'JJ-TL',
         'NN$':'NN', 'NN$-HL':'NN', 'NN$-TL':'NN', 'NNS$':'NN', 'NNS$-TL':'NN',
         'NNS-TL-HL':'NNS-TL', 'NR$-TL':'NR$', 'PN-HL':'PN', 'PP$-HL':'PP$',
         'PP$-TL':'PP$', 'PPL-HL':'PPL', 'PPO-HL':'PPO', 'PPO-TL':'PPO',
         'PPS+HVZ':'PPS+BEZ', 'PPSS+HVD':'PPSS+MD', 'PPSS-HL':'PPSS',
         'PPSS-TL':'PPSS', 'RB-NC':'RB', 'VBD-HL':'VBD', 'VBN-TL-HL':'VBN-TL',
         'WDT-HL':'WDT', 'WRB-HL':'WRB'}
tagdict = {tag:tag for tag in tag_list}
tagdict.update(marge)

#update tag set with simple tag dict.
test_tags = [tagdict[tag] for tag in test_tags]
gold_tags = [tagdict[tag] for tag in gold_tags]
print('simplified tagger accuracy : %.4f' % nltk.accuracy(gold_tags, test_tags))

