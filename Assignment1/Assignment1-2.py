from nltk.corpus import stopwords as sw
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

sentenceToExtract = "With some of hacks to your line of code , we can simply extract the data you need ."
ps = PorterStemmer()

stopList = sw.words('english')
newStopWords = """with some your just have from it's /via &amp; that they your there this into providing would can't"""
stopList += newStopWords.split()
newStopsRemoved = [word for word in sentenceToExtract.lower().split() if word not in stopList]
print('Original Sentence: ')
print(sentenceToExtract)
print("\nAfter addition of new Words: ")
print(" ".join(newStopsRemoved))
for w in newStopsRemoved:
    print(ps.stem(w))