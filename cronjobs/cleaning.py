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
# data = stop_factory.get_stop_words()

# Standar Word Checker
dictFile = os.path.dirname(os.path.realpath(__file__))+"/improveDict.txt"
swChecker = SWChecker(dictFile)
prosaHelper = Prosa()
# print(dictFile)

sentence = "saya menginginkan barang saya kembali lagi seperti sedia kala saat Tuhan menciptakan" 

standardSentence = swChecker.check(sentence)

stopwordsSentence = stopword.remove(standardSentence)

normalizeSentence = prosaHelper.normalize(stopwordsSentence)

stemmedSentence = stemmer.stem(normalizeSentence)

