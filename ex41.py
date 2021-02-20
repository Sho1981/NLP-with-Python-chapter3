# -*- coding: utf-8 -*-

words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']

vsequences = set()

for word in words:
	vowels = []
	for char in word:
		if char in 'aeiou':
            vowels.append(char)
	vsequences.add(''.join(vowels))

print(sorted(vsequences))

print(sorted([''.join([char for char in word if char in 'aeiou']) for word in words]))

