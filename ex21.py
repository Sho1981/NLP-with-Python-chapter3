# -*- coding: utf-8 -*-

import nltk
import urllib
import re

WEBPAGE =  "https://en.wikipedia.org/wiki/Steve_Jobs"

def unknown(url):
	rawtext = urllib.request.urlopen(url).read()
	tokens = re.findall(r'[(^a-zA-Z)][a-zA-Z]+[(^a-zA-Z)]', rawtext.decode())

	wnl = nltk.WordNetLemmatizer()
	tokens_wnl = []
	for w in tokens:
		word = (re.sub(r'[\W]', '', w)).lower()
		tokens_wnl.append(wnl.lemmatize(word))

	english_vocab = set(w.lower() for w in nltk.corpus.words.words())

	return [w for w in set(tokens_wnl) if not(w in english_vocab)]

list = unknown(WEBPAGE)
print(list)

