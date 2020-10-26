import requests
from bs4 import BeautifulSoup

# TODO create list of tables based on page showing current status
urls = [
    'http://hands.wrgpt.org/a/a1.html',
    'http://hands.wrgpt.org/a/a2.html',
    'http://hands.wrgpt.org/a/a3.html',
    'http://hands.wrgpt.org/a/a4.html',
    'http://hands.wrgpt.org/a/a5.html',
    'http://hands.wrgpt.org/a/a6.html',
    'http://hands.wrgpt.org/a/a7.html',
    'http://hands.wrgpt.org/a/a8.html',
    'http://hands.wrgpt.org/a/a9.html',
]

tableList = dict()

for url in urls:
    response = requests.get(url)
    table = url[25:27]
    soup = BeautifulSoup(response.text, 'lxml')
    preTags = soup.select('pre')
    for pTag in preTags:
        if pTag.text[:5].strip() != 'HAND':
            text = pTag.text.strip()
            tableList[table] = text.splitlines()

for tbl in tableList.values():
    print(tbl)

#
#
#
# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# tags = soup.find_all('div', class_='tags')
#
# for i in range(len(quotes)):
#     print(quotes[i].text)
#     print(authors[i].text)
#     quoteTags = tags[i].find_all('a', class_='tag')
#     for quoteTag in quoteTags:
#         print(quoteTag.text)
