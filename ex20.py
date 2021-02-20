# -*- coding: utf-8 -*-

import nltk
import urllib
import re

WEATHER_NEWS =  "https://www.japantimes.co.jp/weather/"
OUTPUT_FILE = "output.txt"

CITY = ['Tokyo', 'Osaka', 'Nagoya']

rawtext = urllib.request.urlopen(WEATHER_NEWS).read()

tokens = re.split(r'<[a-zA-Z0-9/\s\!\"-=_\.\n\?\(\)\:]*>', rawtext.decode())

print(type(tokens))

day_index = tokens.index('Day')
cities_index = [(word, tokens.index(word)) for word in CITY]



#print(day_index, cities_index)

daylist = [w for w in tokens[day_index:day_index+20] if re.search('day$', w)]

print()
print('%8s' % '', end = '')
for w in daylist:
	print('%12s' % w, end = '')
print()

cities_temp = []

for i in range(len(CITY)):
	print('%8s' % CITY[i], end = '')
	for w in tokens[cities_index[i][1]:cities_index[i][1]+30]:
		if re.search(r'.*[(&#8451)℃].*', w):
			w2 = w.replace('&#8451', '℃')
			temp = re.findall(r'-?[0-9]+℃', w2)
			print('%10s' % (temp[0]+'/'+temp[1]), end ='')
	print()

#print(tokens[cities_index[0][1]:cities_index[0][1]+30])

#print(tokens[cities_index[1][1]:cities_index[1][1]+30])


