# Jonah Berger, Contagious https://www.youtube.com/watch?v=iRMdvhBiOQU

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

# # Abaikan ini pekerjaan saya, belum beres
# s = 'Aku pernah mendengar Aisya bercerita bahwa sebenarnya ia tidak terlalu senang dengan kabar perjodohan yang diatur oleh orang tuanya.'
 
# #Create factory
# stop_factory = StopWordRemoverFactory()
 
# # Tambahkan Stopword Baru
# data = stop_factory.get_stop_words() #+more_stopword
 
# stopword = stop_factory.create_stop_word_remover()
# print(s)
# print(stopword.remove(s))
# print(data)

# # # stopwords remove
# # stop_factory = StopWordRemoverFactory()
# # more_stopword = ['dengan', 'ia','bahwa','oleh', 'aja', 'nih', 'yg', 'nge']
# # data = stop_factory.get_stop_words()+more_stopword
# # stopword = stop_factory.create_stop_word_remover()

# # kalimat = 'Mangga akang" celana jeans nya.. Warna hanya hitam aja.. Size kumplit.. 082217089975'
# # stop = stopword.remove(kalimat)
# # print(stop)

# Get personal profile
InstagramAPI.getProfileData()
result = InstagramAPI.LastJson
print(result)

# Get from timeline
InstagramAPI.timelineFeed()
result = InstagramAPI.LastJson
feeds = result['items']

for x in range(len(feeds)):
	print("----START-----")
	try:
		sentence = feeds[x]['caption']['text']
		timestamp = datetime.utcfromtimestamp(feeds[x]['caption']['created_at']).strftime('%Y-%m-%d %H:%M:%S')
		like_count = feeds[x]['like_count']
		print("Caption -> ", sentence)
		print("Timestamp -> ", timestamp)
		print("Like Count -> ", like_count)
		output = stemmer.stem(sentence)
		print("Stemming -> ", output)
	except Exception as e:
		print("Tidak ada text") 
	else:
		pass
	finally:
		pass
	# print(feeds[x])
	print("----END-----\n")


# Standard words checker
print("----STANDARD WORDS CHECKER-----")
dictFile = os.path.dirname(os.path.realpath(__file__))+"/improveDict.txt"
swChecker = SWChecker(dictFile)

# text = "Nah, buat nemenin pagi kamu gimana kalau hapal aja"
# text = "Saya adalah seorang atlit tauladan esei aja"
# print(text)
# stdText = swChecker.check(text)
# print(stdText)

for x in range(len(feeds)):
	print("----START-----")
	try:
		originalSentence = feeds[x]['caption']['text']
		print("Original -> ", originalSentence)
		standardSentence = swChecker.check(originalSentence)
		print("Standard -> ", standardSentence)
	except Exception as e:
		print("Tidak ada text") 
	else:
		pass
	finally:
		pass
	print("----END-----\n")