from InstagramAPI import InstagramAPI
from datetime import datetime
from Database.DB import DB

# Set username will be used
target = ['infobandungkuliner', 'bandung_eatery', 'duniakulinerbandung', 'esxplorebandung', 'bandungkunafe', 'bandung.banget', 'kulinerbandung', 'duniakulinerbdg', 'foodstories', 'bandungmakuta']

# Login
username="contact_me"
InstagramAPI = InstagramAPI(username, "contact_me")
InstagramAPI.login()

# Database
db = DB('Database\\stepps.db')
db.connect()

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


def searchByUsername(username):

	print('====================')
	try:
		# Get username and pk info
		InstagramAPI.searchUsername(username);
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

					saveData = {'username': username, 'follower_count': dataFollower, 'taken_at': item['taken_at'], 'like_count': dataLike, 'caption_text': item['caption']['text'], 'time_frame': timeFrame, 'engagement': engagement, 'created_at': created}

					db.insertIntoCrawlingTable(saveData)
		else:
			print('Account is private')

	except:
		print('Problem with username :', username)
	
	print('====================')

for item in target:
	searchByUsername(item)

db.close()