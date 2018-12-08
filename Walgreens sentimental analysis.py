# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 19:47:31 2018

@author: 13pra
"""

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



wallgreens_2017 = open('2017_management_discussion.txt').read()
wallgreens_2016 = open('2016_management_discussion.txt').read()
wallgreens_2015 = open('2015_management_discussion.txt').read()

negative_Word = pd.read_csv('LM_neg_words.txt', header=None)
positive_word = pd.read_csv('LM_pos_words.txt', header=None)
negative_Word = list(negative_Word[0].str.lower())
positive_word = list(positive_word[0].str.lower())

words_2017 = word_tokenize(wallgreens_2017)
words_2016 = word_tokenize(wallgreens_2016)
words_2015 = word_tokenize(wallgreens_2015)

negative_2017 = []
negative_2016 = []
negative_2015 = []
positive_2017 = []
positive_2016 = []
positive_2015 = []
negative_2017_count = 0
negative_2016_count = 0
negative_2015_count = 0
positive_2017_count = 0
positive_2016_count = 0
positive_2015_count = 0


final_2017 = []
final_2016 = []
final_2015 = []


for word in words_2017:
    word = word.lower()
    if word.isalpha():
        final_2017.append(word)

for word in words_2016:
    word = word.lower()
    if word.isalpha():
        final_2016.append(word)

for word in words_2015:
    word = word.lower()
    if word.isalpha():
        final_2015.append(word)



total_words_2017 = len(final_2017)  # 13462
total_words_2016 = len(final_2016)  # 12647
total_words_2015 = len(final_2015)  # 12916

stopWords = set(stopwords.words("english"))

freqTable_2017 = dict()
for i in range(len(final_2017)):
    if final_2017[i] in freqTable_2017:
        freqTable_2017[final_2017[i]] += 1
    else:
        freqTable_2017[final_2017[i]] = 1


freqTable_2016 = dict()
for i in range(len(final_2016)):
    if final_2016[i] in freqTable_2016:
        freqTable_2016[final_2016[i]] += 1
    else:
        freqTable_2016[final_2016[i]] = 1


freqTable_2015 = dict()
for i in range(len(final_2015)):
    if final_2015[i] in freqTable_2015:
        freqTable_2015[final_2015[i]] += 1
    else:
        freqTable_2015[final_2015[i]] = 1

freqTable_2017 = {key: freqTable_2017[key] for key in sorted(freqTable_2017, key=freqTable_2017.get, reverse=True)}
freqTable_2016 = {key: freqTable_2016[key] for key in sorted(freqTable_2016, key=freqTable_2016.get, reverse=True)}
freqTable_2015 = {key: freqTable_2015[key] for key in sorted(freqTable_2015, key=freqTable_2015.get, reverse=True)}


stopwords_2017 = []
for i in range(len(final_2017)):
    if final_2017[i] in stopWords:
        stopwords_2017.append(final_2017[i])


stopwords_2016 = []
for i in range(len(final_2016)):
    if final_2016[i] in stopWords:
        stopwords_2016.append(final_2016[i])


stopwords_2015 = []
for i in range(len(final_2015)):
    if final_2015[i] in stopWords:
        stopwords_2015.append(final_2015[i])


len(stopwords_2017) #4975
len(stopwords_2016) # 4741
len(stopwords_2015) #4897

new_stopwords = stopWords - {'no', 'not', 'never'}
new_2017_words = freqTable_2017.keys() - (new_stopwords)
new_2016_words = freqTable_2016.keys() - (new_stopwords)
new_2015_words = freqTable_2015.keys() - (new_stopwords)


for word in new_2017_words:
    if word in negative_Word:
        negative_2017.append(word)
        negative_2017_count += freqTable_2017[word]
    if word in positive_word:
        positive_2017.append(word)
        positive_2017_count += freqTable_2017[word]

for word in new_2016_words:
    if word in negative_Word:
        negative_2016.append(word)
        negative_2016_count += freqTable_2016[word]
    if word in positive_word:
        positive_2016.append(word)
        positive_2016_count += freqTable_2016[word]

for word in new_2015_words:
    if word in negative_Word:
        negative_2015.append(word)
        negative_2015_count += freqTable_2015[word]
    if word in positive_word:
        positive_2015.append(word)
        positive_2015_count += freqTable_2015[word]

#positive words in documents of each year
print(positive_2017)
print(positive_2015)
print(positive_2016)


#negative words in documents of each year
print(negative_2016)
print(negative_2017)
print(negative_2015)

total_words_2017_new = 0
for word in new_2017_words:
    total_words_2017_new += freqTable_2017[word]


total_words_2016_new = 0
for word in new_2016_words:
    total_words_2016_new += freqTable_2016[word]


total_words_2015_new = 0
for word in new_2015_words:
    total_words_2015_new += freqTable_2015[word]


# positive-negetive/total words ratios
print((positive_2017_count - negative_2017_count)/total_words_2017_new)
print((positive_2016_count - negative_2016_count)/total_words_2016_new)
print((positive_2015_count - negative_2015_count)/total_words_2015_new)

#negetive words ratios
print(negative_2017_count/total_words_2017_new)
print(negative_2016_count/total_words_2016_new)
print(negative_2015_count/total_words_2015_new)

#positive words ratios
print(positive_2017_count/total_words_2017_new)
print(positive_2016_count/total_words_2016_new)
print(positive_2015_count/total_words_2015_new)


# does the documents have negative words?
negator_words = ['no', 'not', 'never']

flag_2017 = False
for word in freqTable_2017:
    if word in negator_words:
        flag_2017 = True


flag_2016 = False
for word in freqTable_2016:
    if word in negator_words:
        flag_2016 = True


flag_2015 = False
for word in freqTable_2015:
    if word in negator_words:
        flag_2015 = True

sent_text_2017 = nltk.sent_tokenize(wallgreens_2017)
negator_positive_2017 = []

for i in range(3):
    for sentence in sent_text_2017:
        spt_sent = sentence.replace('\n', ' ')
        list_sent = spt_sent.split(' ')
        for index, word in enumerate(list_sent):
            if negator_words[i] == word:
                neg_pos = int(index)
                lower_pos = neg_pos - 3
                upper_pos = neg_pos + 3
                if lower_pos < 0:
                    lower_pos = 0
                if upper_pos > len(list_sent):
                    upper_pos = len(list_sent)
                for j in range(len(positive_2017)):
                    if positive_2017[j] in list_sent[lower_pos:upper_pos+1]:
                        negator_positive_2017.append(positive_2017[j])

print('Positive words around negative word in 2017',negator_positive_2017)


sent_text_2016 = nltk.sent_tokenize(wallgreens_2016)
negator_positive_2016 = []

for i in range(3):
    for sentence in sent_text_2016:
        spt_sent = sentence.replace('\n', ' ')
        list_sent = spt_sent.split(' ')
        for index, word in enumerate(list_sent):
            if negator_words[i] == word:
                neg_pos = int(index)
                lower_pos = neg_pos - 3
                upper_pos = neg_pos + 3
                if lower_pos < 0:
                    lower_pos = 0
                if upper_pos > len(list_sent):
                    upper_pos = len(list_sent)
                for j in range(len(positive_2016)):
                    if positive_2016[j] in list_sent[lower_pos:upper_pos+1]:
                        negator_positive_2016.append(positive_2016[j])

print('Positive words around negative word in 2016',negator_positive_2016)


sent_text_2015 = nltk.sent_tokenize(wallgreens_2015)
negator_positive_2015 = []

for i in range(3):
    for sentence in sent_text_2015:
        spt_sent = sentence.replace('\n', ' ')
        list_sent = spt_sent.split(' ')
        for index, word in enumerate(list_sent):
            if negator_words[i] == word:
                neg_pos = int(index)
                lower_pos = neg_pos - 3
                upper_pos = neg_pos + 3
                if lower_pos < 0:
                    lower_pos = 0
                if upper_pos > len(list_sent):
                    upper_pos = len(list_sent)
                for j in range(len(positive_2015)):
                    if positive_2015[j] in list_sent[lower_pos:upper_pos+1]:
                        negator_positive_2015.append(positive_2015[j])



print('Positive words around negative word in 2015',negator_positive_2015)







