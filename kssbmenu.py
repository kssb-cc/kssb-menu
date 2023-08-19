import requests
from bs4 import BeautifulSoup


class KssbMenu:
    def __init__(self):
        self.url = "https://kssb.net/parents/menus/"
        self.session = requests.session()

    def download(self):
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.text, features="html.parser")
        menu = {}
        for front, back in zip(
            soup.find_all("div", class_="vc-hoverbox-front-inner"),
            soup.find_all("div", class_="vc-hoverbox-back-inner"),
        ):
            day = front.text[1:-1]
            menu[day] = "\n".join([p.text for p in back.find_all("p")])
        return menu
