from bs4 import BeautifulSoup
import requests
import re

page = requests.get('https://es.wikipedia.org/wiki/Python')
soup = BeautifulSoup(page.content,'html.parser')

# Extenal refs
for link in soup.findAll('a',attrs={'href': re.compile('^http://')}):
    print(link.get('href'))

"""
baselink = 'https://es.wikipedia.org'

for link in soup.findAll('a'):
    if str(link.get('href'))[0] == '/':
        print(baselink + link.get('href'))
"""

baselink = 'https://es.wikipedia.org'

for link in soup.findAll('a'):
    if str(link.get('href'))[0] == '/' and str(link.get('href'))[1] != '/':
        print(baselink + link.get('href'))
