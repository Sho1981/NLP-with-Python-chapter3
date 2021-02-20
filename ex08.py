import nltk
import urllib
import re

def html_remove(url):
	raw_contents = urllib.request.urlopen(url).read()

	return ''.join(re.split(r'<[a-zA-Z0-9/\s\!\"-=_\.\n]*>', raw_contents.decode()))
