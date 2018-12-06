import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from datetime import datetime
import os.path
from SWChecker.SWChecker import SWChecker
from OHelper.Prosa import Prosa

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Stopword Removal
stop_factory = StopWordRemoverFactory()
stopword = stop_factory.create_stop_word_remover()
data = stop_factory.get_stop_words()

# Standar Word Checker
dictFile = os.path.dirname(os.path.realpath(__file__))+"/improveDict.txt"
swChecker = SWChecker(dictFile)
prosaHelper = Prosa()
# print(dictFile)

sentence = "" 
print("Raw -> ", sentence)
standardSentence = swChecker.check(sentence)
print("standardSentence -> ", standardSentence)
stopwordsSentence = stopword.remove(standardSentence)
print("stopwordsSentence -> ", stopwordsSentence)
normalizeSentence = prosaHelper.normalize(sentence)
print("normalizeSentence -> " ,normalizeSentence)
stemmedSentence = stemmer.stem(normalizeSentence)
print("stemmedSentence -> ", stemmedSentence)
