# -*- coding: utf-8 -*-

import nltk

def load(f): #f:file name

	ftext = open(f, encoding = 'utf-8')
	filetext = ftext.read()

	return filetext

#print(load("corpus.txt"))

text = load("corpus.txt")

pattern = r'''(?x)
				([ぁ-んァ-ン一-龥]+)
				|[。．、，]
'''

print(nltk.regexp_tokenize(text, pattern))
