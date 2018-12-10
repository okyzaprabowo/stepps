from InstagramAPI import InstagramAPI
from datetime import datetime
from Database.DB import DB

import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from collections import Counter
import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import os.path
from SWChecker.SWChecker import SWChecker
from OHelper.Prosa import Prosa
from Database.DB import DB

# Set username will be used
target = ['infobandungkuliner', 'bandung_eatery', 'duniakulinerbandung', 'esxplorebandung', 'bandungkunafe', 'bandung.banget', 'kulinerbandung', 'duniakulinerbdg', 'foodstories', 'bandungmakuta']

# Login
username="na_ratnaa"
InstagramAPI = InstagramAPI(username, "ratnasanti123")
InstagramAPI.login()

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()
prosaHelper = Prosa()

# Stopword Removal
stop_factory = StopWordRemoverFactory()
stopword = stop_factory.create_stop_word_remover()
data = stop_factory.get_stop_words()

# Standar Word Checker
dictFile = os.path.dirname(os.path.realpath(__file__))+"/improveDict.txt"
swChecker = SWChecker(dictFile)

# Database
db = DB('/home/vagrant/code/InstaCrawler/stepps/app/db.sqlite3')
db.connect()

def steppsLabeling(self_class):
	if(self_class == 0):
		return "sc"
	if(self_class == 1):
		return "t"
	if(self_class == 2):
		return "e"
	if(self_class == 3):
		return "pu"
	if(self_class == 4):
		return "pr"
	if(self_class == 5):
		return "st"

def classify(stemmedSentence):
    df = pd.read_csv('/home/vagrant/code/InstaCrawler/stepps/NaiveBayes/alltab.tsv', sep='\t', lineterminator='\r')

    counter = Counter(df['label'].tolist())
    top_10_varieties = {i[0]: idx for idx, i in enumerate(counter.most_common(10))}
    df = df[df['label'].map(lambda x: x in top_10_varieties)]

    description_list = df['text'].tolist()
    varietal_list = [top_10_varieties[i] for i in df['label'].tolist()]
    varietal_list = np.array(varietal_list)

    count_vect = CountVectorizer()
    x_train_counts = count_vect.fit_transform(description_list)


    tfidf_transformer = TfidfTransformer()
    x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

    train_x, test_x, train_y, test_y = train_test_split(x_train_tfidf, varietal_list, test_size=0.3)

    clf = LinearSVC().fit(train_x, train_y)
    y_score = clf.predict(test_x)

    print(stemmedSentence.split())

    # array prediction
    prediction_array = clf.predict(count_vect.transform(stemmedSentence.split()))
    text_array = stemmedSentence.split()
    print(steppsLabeling(prediction_array[0]), text_array[0])
    count=0
    for text in text_array:
    	print(steppsLabeling(prediction_array[count]), text_array[count])
    	created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    	save_data = {'keyword': text_array[count], 'label': steppsLabeling(prediction_array[count]), 'created_at': created}
    	db.insertIntoClassifyTable(save_data)
    	count=count+1

def getTimeFrame(time):
	# 02:00 - 07:59
	if((time.hour > 2 and time.minute > 0) and (time.hour < 7 and time.minute < 59)):
		return 1
	# 08:00 - 12:59
	elif((time.hour > 8 and time.minute > 0) and (time.hour < 12 and time.minute < 59)):
		return 2
	# 13:00 - 15:59
	elif((time.hour > 13 and time.minute > 0) and (time.hour < 15 and time.minute < 59)):
		return 3
	# 16:00 - 17:59
	elif((time.hour > 16 and time.minute > 0) and (time.hour < 17 and time.minute < 59)):
		return 4
	# 18:00 - 21:59
	elif((time.hour > 18 and time.minute > 0) and (time.hour < 21 and time.minute < 59)):
		return 5
	# 22:00 - 01:59
	# else if((time.hour > 22 && time.minute > 0) && (time.hour < 1 && time.minute < 59))
	else:
		return 6

# def calculate_result(keyword):



def searchByUsername(username):

	print('====================')
	try:
		# Get username and pk info
		InstagramAPI.searchUsername(username)
		data = InstagramAPI.LastJson
		userpk = data['user']['pk']
		print('Searching posts data with username :', username, ' (', userpk,')')
		dataFollower = data['user']['follower_count']
		print('Total Follower: ', dataFollower)
		userPrivate = data['user']['is_private']
		if userPrivate == False:
			# Use `getTotalUserFeed` to fetch all of content
			# Use `getUserFeed` to fetch list manual (limited environment solution :D)
			InstagramAPI.getUserFeed(userpk)
			data = InstagramAPI.LastJson
			# print('Total current posts : ', data['num_results'])
			items = data['items']
			if len(items) > 0:
				for item in items:
					dataLike = item['like_count']
					time = datetime.utcfromtimestamp(item['taken_at'])
					print('Timestamp : ', item['taken_at'], ' (', time.strftime('%Y-%m-%d %H:%M:%S'), ') with total Likes: ', dataLike, ' Text : ', item['caption']['text'])
					
					timeFrame = getTimeFrame(time)
					engagement = 'L'
					likePerFollower = dataLike/dataFollower
					lpfPercentage = likePerFollower * 100
					if(lpfPercentage > 2 and lpfPercentage <= 5):
						engagement = 'M'
					elif(lpfPercentage > 5):
						engagement = 'H'
					created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

					saveData = {'username': username, 'follower_count': dataFollower, 'taken_at': time, 'like_count': dataLike, 'caption_text': item['caption']['text'], 'time_frame': timeFrame, 'engagement': engagement, 'created_at': created}

					db.insertIntoCrawlingTable(saveData)
					sentence = item['caption']['text']
					standardSentence = swChecker.check(sentence)
					stopwordsSentence = stopword.remove(standardSentence)
					stemmedSentence = stemmer.stem(stopwordsSentence)
					print("Raw -> ", sentence)
					print("Stemming -> ", stemmedSentence)
					classify(stemmedSentence)
		else:
			print('Account is private')

	except:
		print('Problem with username :', username)
	
	print('====================')

for item in target:
	searchByUsername(item)

# cur = db.connect().cursor()
# cur.execute("SELECT * FROM dashboard_classificationresult")
# rows = cur.fetchall()
# for row in rows:
# 	print(row[1])
# 	cur.execute("SELECT COUNT(*) FROM dashboard_crawling WHERE engagement = 'H' AND caption_text LIKE '%?%'", (row[1],))
# 	h_keyword_count = len(cur.fetchall())
# 	print(h_keyword_count)
	

db.close()