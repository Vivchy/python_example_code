import requests
from time import sleep




def reque():
    wiki = requests.get('https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D1%80%D1%80%D0%B5%D0%BB_(%D1%83%D0%B7%D0%B5%D0%BB)')
    print(wiki.status_code)

reque()