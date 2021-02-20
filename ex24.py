# -*- coding: utf-8 -*-

import nltk
import re

def hAck3r(text):   #text: str

	words = [w.lower() for w in nltk.word_tokenize(text)]

	w_after = []

	for w in words:
		w = re.sub(r'e', '3', w)
		w = re.sub(r'i', '1', w)
		w = re.sub(r'o', '0', w)
		w = re.sub(r'1', '|', w)
		w = re.sub(r'^s', '$', w)
		w = re.sub(r's', '5', w)
		w = re.sub(r'\.', '5w33t!', w)
		w = re.sub(r'ate', '8', w)
		w_after.append(w)

	return ' '.join(w_after)

raw = "'When I'M a Duchess,' she said to herself, (not in a very hopeful tone though), 'I won't have any pepper in mu kitchen AT ALL. Soup dose very well without--Maybe it's always pepper that makes people hot-tempered,'..."

print(hAck3r(raw))

