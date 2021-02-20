# -*- coding: utf-8 -*-

import nltk
import re

def pig_latin(word):	#word: str

	split = re.findall(r'^([bcdfghjklmnpqrstvwxyz]*?)([aeiou]+.*)$', word.lower())
	if split == []:
		split = [(word, '')]
	[(foward, back)] = split
	return back + foward + 'ay'

def pl_line(text):		#text: long sentense

	words = []

	for w in text.split():
		ww = re.sub(r'[^a-zA-Z]', '', w.lower())
		if not(ww == ''):
			words.append(pig_latin(ww))
		else:
			words.append('error')
	return ' '.join(words)

raw = "'When I'M a Duchess,' she said to herself, (not in a very hopeful tone though), 'I won't have any pepper in my kitchen AT ALL. Soup dose very well without--Maybe it's always pepper that makes people hot-tempered,'..."

print(pl_line(raw))


