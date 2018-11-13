from InstagramAPI import InstagramAPI
from datetime import datetime

# Set username will be used
target = ['infobandungkuliner', 'bandung_eatery', 'duniakulinerbandung', 'esxplorebandung', 'bandungkunafe', 'bandung.banget', 'kulinerbandung', 'duniakulinerbdg', 'foodstories', 'bandungmakuta']

# Login
username="na_ratnaa"
InstagramAPI = InstagramAPI(username, "ratnasanti123")
InstagramAPI.login()

def searchByUsername(username):
	print('====================')
	try:
		# Get username and pk info
		InstagramAPI.searchUsername(username);
		data = InstagramAPI.LastJson
		userpk = data['user']['pk']
		print('Searching posts data with username :', username, ' (', userpk,')')
		print('Total Follower: ', data['user']['follower_count'])
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
					print('Timestamp : ', item['taken_at'], ' (', datetime.utcfromtimestamp(item['taken_at']).strftime('%Y-%m-%d %H:%M:%S'), ') with total Likes: ', item['like_count'])
		else:
			print('Account is private')

	except:
		print('Problem with username :', username)
	
	print('====================')

for item in target:
	searchByUsername(item)
