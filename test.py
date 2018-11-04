import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from datetime import datetime
import os.path
from SWChecker.SWChecker import SWChecker

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
# print(dictFile)

sentence = "Tolongin gw dong"
# sentence = "Tolongin gw dong"
stopwordsSentence = stopword.remove(sentence)
standardSentence = swChecker.check(stopwordsSentence)
stemmedSentence = stemmer.stem(standardSentence)
print("Raw -> ", sentence)
print("Result -> ", stemmedSentence)