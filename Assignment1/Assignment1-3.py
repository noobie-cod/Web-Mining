import urllib.request
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords as sw
from nltk.stem import PorterStemmer
import nltk.data
import os

url = "http://quotes.toscrape.com/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html5lib").text
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
tokenizer.tokenize(soup.strip())
wordList = re.findall(r'\w+',soup)
stopList = sw.words('english')
newStopsRemoved = [word for word in wordList if word not in stopList]
print(" ".join(newStopsRemoved))
pathToFile = '/Users/aritropaul/Documents/Fall Sem 2018-19/Web Mining/Lab/Lab2/corpus.txt'
fo = open(pathToFile, "w+")
for item in newStopsRemoved:
    fo.write(item)
    fo.write('\n')
fo.close()

searchword = input("Enter word to search for: ")
text = nltk.Text(nltk.word_tokenize(soup))
print(text.concordance(searchword))

