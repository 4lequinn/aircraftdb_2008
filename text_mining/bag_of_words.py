import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

from nltk.stem import SnowballStemmer

text = open('el_quijote.txt','r').read()
phrases = sent_tokenize(text)
#print(phrases)

words = word_tokenize(text.lower())
#print(words)

# Top 20
fdist = FreqDist(words)
#print(fdist.most_common(20))

# Unnecessary and/or uninformative words
stop_words = stopwords.words('spanish')
#print(stop_words)

words2 = [x for x in words if x not in stop_words + list(string.punctuation)]
#print(words2)

# Top 10
fdist2 = FreqDist(words2)
print(fdist2.most_common(10))


stemmer = SnowballStemmer('spanish')

word_root = []

for word in words2:
    word_root.append(stemmer.stem(word))

# print(raices)
print(FreqDist(word_root).most_common(10))