import urllib.request
from bs4 import BeautifulSoup
import re
import pprint

def cleanPage(text):
    clean = re.compile('<.*?>')
    return re.sub(clean,"",text)

def getWords(text):
    count = len(re.findall(r'\w+',text))
    return count

url = input('Enter url\n')
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html5lib").text
wordList = re.findall(r'\w+',soup)
wordFrequency = [wordList.count(w) for w in wordList]

print("No. of words in the page =  ")
print(getWords(soup))
print("Word Frequencies = ")
print(list(zip(wordList,wordFrequency)))