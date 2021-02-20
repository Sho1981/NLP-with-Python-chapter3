import nltk
import re

raw = "'When I'M a Duchess,' she said to herself, (not in a very hopeful tone though), 'I won't have any pepper in mu kitchen AT ALL. Soup dose very well without--Maybe it's always pepper that makes people hot-tempered,'..."

print(nltk.re_show(r'[a-zA-Z]+', raw))

