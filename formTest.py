import requests
from bs4 import BeautifulSoup as bs4 

class Form:
	name = "Alex"
	password = "qwerty"
	gmail = "alex@gmail.com"
	url = "itproger.com"

	def __init__(self, name, password, gmail="alex@gmail.com", url="itproger.com"):
		self.name = name
		self.password = password
		self.gmail = gmail
		self.url = url

	def set_web_url(self):
		headers = {
			'accept': '*/*'
		}

		self.url = url
		session = requests.Session()
		req = session(url, headers=headers)
		if self.url == 200:
			print('True')
		else:
			print('False')


alex = Form("Alex", "sfjdjb")
bot = Form("Admin", "1234", "gmail@gmail.ua", "itproger.com")