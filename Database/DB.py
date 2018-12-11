import sqlite3
from datetime import datetime

class DB:
	def __init__(self, dbName, debug = False):
		self.dbName = dbName
		self.debug = debug
		self.connection = False
		if(self.debug):
			print ("Opened database successfully")

	def connect(self):
		self.connection = sqlite3.connect(self.dbName)

	def close(self):
		self.connection.close()

	def createCrawlingTable(self):
		query = '''CREATE TABLE crawling
         (id             INTEGER PRIMARY KEY,
         username        VARCHAR(255),
         follower_count  INTEGER,
         taken_at        TIMESTAMP,
         like_count      INTEGER,
         caption_text    TEXT,
         time_frame      INTEGER,
         engagement      VARCHAR(1),
         created_at      TIMESTAMP);'''

		self.connection.execute(query)

	def insertIntoCrawlingTable(self, data):
		self.connection.execute("INSERT INTO crawling (username,follower_count,taken_at,like_count,caption_text,time_frame,engagement,created_at) VALUES ('%(username)s',%(follower_count)d,'%(taken_at)s',%(like_count)d,'%(caption_text)s',%(time_frame)d,'%(engagement)s','%(created_at)s') " % data)
		self.connection.commit()

	def selectFromCrawlingTable(self, id = 0):
		query = "SELECT id, caption_text FROM crawling"
		if(id > 0):
			where = " WHERE id = " + str(id)
			query = query + where
		return self.connection.execute(query)

	def crawlingTableSeeder(self):
		data = {'username': "testing_username", 'follower_count': 100, 'taken_at': "2018-12-10", 'like_count': 200, 'caption_text': "hari ini sangat menyenangkan", 'time_frame': 1, 'engagement': "M", 'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
		self.insertIntoCrawlingTable(data)

	def createCleaningTable(self):
		query = '''CREATE TABLE cleaning
         (id             INTEGER PRIMARY KEY,
         crawling_id INTEGER,
         standard    TEXT,
         stopwords   TEXT,
         normalize   TEXT,
         stemmed     TEXT,
         created_at  TIMESTAMP);'''

		self.connection.execute(query)

	def insertIntoCleaningTable(self, data):
		self.connection.execute("INSERT INTO cleaning (crawling_id,standard,stopwords,normalize,stemmed,created_at) VALUES (%(crawling_id)d,'%(standard)s','%(stopwords)s','%(normalize)s','%(stemmed)s','%(created_at)s') " % data)
		self.connection.commit()

	def cleaningTableSeeder(self):
		data = {'crawling_id': 1, 'standard': "hari ini sangat menyenangkan", 'stopwords': "hari ini sangat menyenangkan", 'normalize': "hari ini sangat menyenangkan", 'stemmed': "hari ini sangat menyenangkan", 'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
		self.insertIntoCleaningTable(data)