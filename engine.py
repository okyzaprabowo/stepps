# Jonah Berger, Contagious https://www.youtube.com/watch?v=iRMdvhBiOQU
# Crawling Data -> Slangword -> Stopword -> Stemming -> STEPPS clustering
# Reference:
# Pramudita, (2011) "PENERAPAN ALGORITMA STEMMING NAZIEF & ADRIANI DAN SIMILARITY PADA PENERIMAAN JUDUL THESIS"
# Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 61
# Zulfa, Ira. (2017) "Sentimen Analisis Tweet Berbahasa Indonesia dengan Deep Belief Network"

from InstagramAPI import InstagramAPI
import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from datetime import datetime
import os.path
from SWChecker.SWChecker import SWChecker

# Login
username="na_ratnaa"
InstagramAPI = InstagramAPI(username, "ratnasanti123")
InstagramAPI.login()

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
print(dictFile)

# Get from timeline
InstagramAPI.timelineFeed()
result = InstagramAPI.LastJson
feeds = result['items']

print("----CRAWLING FROM INSTAGRAM-----")
for x in range(len(feeds)):
	print("----START-----")
	try:
		sentence = feeds[x]['caption']['text']
		timestamp = datetime.utcfromtimestamp(feeds[x]['caption']['created_at']).strftime('%Y-%m-%d %H:%M:%S')
		like_count = feeds[x]['like_count']
		print("Caption -> ", sentence)
		print("Timestamp -> ", timestamp)
		print("Like Count -> ", like_count)
		stopwordsSentence = stopword.remove(sentence)
		standardSentence = swChecker.check(stopwordsSentence)
		stemmedSentence = stemmer.stem(standardSentence)
		print("Stemming -> ", stemmedSentence)
	except Exception as e:
		print("Tidak ada text") 
	else:
		pass
	finally:
		pass
	# print(feeds[x])
	print("----END-----\n")