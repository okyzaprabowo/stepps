import requests
import json

class Prosa:
	def __init__(self):
		self.apiKey = "JWJ0kKvmkmC77RW9VUcEAYWi7QTLbSucRC3bNL7c"
	def normalize(self, text):
		url = 'https://api.prosa.ai/v1/normals'
		payloads = {
			"text" : text
		}
		headers = {"Content-Type" : "application/json",
			"x-api-key" : self.apiKey}
		r = requests.post(url, data=json.dumps(payloads), headers=headers)
		return r.json()['normalized_text']