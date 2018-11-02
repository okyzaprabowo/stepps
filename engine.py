# Jonah Berger, Contagious https://www.youtube.com/watch?v=iRMdvhBiOQU test

from InstagramAPI import InstagramAPI
import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from datetime import datetime

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Stopword Removal
stop_factory = StopWordRemoverFactory()
stopword = stop_factory.create_stop_word_remover()
data = stop_factory.get_stop_words()
# print(data)

# stem example
a = "tolongin"
print(stemmer.stem(a))


# Login
# username="na_ratnaa"
# InstagramAPI = InstagramAPI(username, "ratnasanti123")
# InstagramAPI.login()

# Get personal profile
# InstagramAPI.getProfileData()
# result = InstagramAPI.LastJson
# print(result)

# Get from timeline
# InstagramAPI.timelineFeed()
# result = InstagramAPI.LastJson
# feeds = result['items']

# for x in range(len(feeds)):
# 	print("----START-----")
# 	try:
# 		sentence = feeds[x]['caption']['text']
# 		timestamp = datetime.utcfromtimestamp(feeds[x]['caption']['created_at']).strftime('%Y-%m-%d %H:%M:%S')
# 		like_count = feeds[x]['like_count']
# 		print("Caption -> ", sentence)
# 		print("Timestamp -> ", timestamp)
# 		print("Like Count -> ", like_count)
# 		output = stemmer.stem(sentence)
# 		print("Stemming -> ", stopword.remove(output))
# 	except Exception as e:
# 		print("Tidak ada text") 
# 	else:
# 		pass
# 	finally:
# 		pass
# 	# print(feeds[x])
# 	print("----END-----\n")
