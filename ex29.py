# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import brown

CATEGORIES = ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']

def ari_score(ws, ss):	#ws: word list, ss: sentense list

	len_words_ave = sum(len(w) for w in ws) / len(ws)

	len_sents_ave = sum(len(s) for s in ss) / len(ss)

	return 4.7*len_words_ave + 0.5*len_sents_ave - 21.43

cat = 'news'

print('<<< ARI SCORE >>>')

for w in CATEGORIES:

	words = brown.words(categories = w)
	sents = brown.sents(categories = w)
	print('%16s %6.2f' % (w, ari_score(words, sents)))


