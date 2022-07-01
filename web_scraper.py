import requests
import string
from bs4 import BeautifulSoup
import os


def def_title(title):
    new_title = title.replace(' ', '_').strip()
    punctuation = string.punctuation
    for i in punctuation:
        if i in new_title and i != '_':
            new_title = new_title.replace(i, '')
    return new_title

n_page = int(input())
type_page = input()

URL = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page='
for n in range(n_page):
    name_dir = 'Page_' + str(n + 1)
    os.mkdir(name_dir)
    r = requests.get(URL + str(n + 1), headers={'Accept-Language': 'en-US,en;q=0.5'})
    saved_art = []
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.find_all('article')
        for art in articles:
            art_type = art.find('span', {'data-test': 'article.type'}).text.strip()
            if art_type == type_page:
                href = art.find('a', {'data-track-action':'view article'})
                title = def_title(href.text)
                #print(title)
                page = requests.get('https://www.nature.com' + href['href'], headers={'Accept-Language': 'en-US,en;q=0.5'})
                if page.status_code == 200:
                    soup = BeautifulSoup(page.content, 'html.parser')
                    with open(name_dir + '/' + title + '.txt', 'w') as my_file:
                        content = soup.find('div', {'class': 'c-article-body u-clearfix'})
                        my_file.write(content.text.strip())
                    #print('Content saved.')
                    saved_art.append(title)
                else:
                    print('fail')
    else:
        print(f'The URL returned {r.status_code}')
    #print(saved_art)
    print('Saved all articles.')
