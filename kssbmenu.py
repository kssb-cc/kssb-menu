import requests
from bs4 import BeautifulSoup

class kssb_menu():
	def __init__(self):
		self.url="https://kssb.net/parents/menus/"
		self.session=requests.session()
	
	def download(self):
		r=self.session.get(self.url)
		soup=BeautifulSoup(r.text, features="html.parser")
		for t in soup.find_all("div", class_="vc-hoverbox-front-inner"):
			print(f"--Starting heading: {t.text}")
			#The plan was to use this huge 1-line thingy, but not doing that no more so it can be more easily managed / understood. I don't want any more headaches.
			for tag in t.find_all("p", class_="vc-hoverbox-block-inner"):
				print(tag)
			
			print(f"--ending heading {t.text}\n\n")
			
