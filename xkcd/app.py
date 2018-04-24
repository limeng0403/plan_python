import os, sys, re

import bs4, requests

uri = 'https://xkcd.com/'

res = requests.get(uri)

if res.status_code == 200:
    print('ok')
else:
    print('fail')
    exit()

print(res.text)

n = bs4.BeautifulSoup(res.text)
#
divs = n.findAll('div', attrs={'id': 'comic'})

print(len(divs))

if len(divs) == 0:
    print('not find id="comic"')
    exit()
elif len(divs) == 1:
    img = divs[0].findAll('img')

    path = img[0]['src'].split('/')

    if '.' in path[len(path) - 1]:
        print(path[len(path) - 1])

        fileName = path[len(path) - 1]
    else:
        print(path)

        exit()

res = requests.get('https:' + img[0]['src'])

if res.status_code != 200:
    print('img fail')

f = open(fileName, 'wb')

for i in res.iter_content(100000):
    f.write(i)

f.close()

print(os.path.getsize(fileName))
