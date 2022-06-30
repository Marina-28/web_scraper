import requests
import json
from bs4 import BeautifulSoup

url = input("input the URL\n")
if 'title' in url:
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        my_dict = {'title': soup.find('h1').text, 'description': soup.find('span', {'data-testid': 'plot-l'}).text}
        print(my_dict)
else:
    print('Invalid movie page!')
