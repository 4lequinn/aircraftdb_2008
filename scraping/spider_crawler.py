from bs4 import BeautifulSoup
import requests
import time

page = requests.get('https://es.wikipedia.org/wiki/Python')
soup = BeautifulSoup(page.content,'html.parser')

explored = set()
not_explored = set()

baselink = 'https://es.wikipedia.org'

for link in soup.findAll('a'):
    if str(link.get('href'))[0] == '/' and str(link.get('href'))[1] != '/' and baselink + link.get('href') not in explored:
        not_explored.add(baselink + link.get('href'))


while(len(not_explored) != 0 ):
    link = not_explored.pop()
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    print('Links explorados: ',len(explored),'links por explorar: ',len(not_explored))
    explored.add(link)
    time.sleep(1)
    for link in soup.findAll('a'):
        if str(link.get('href'))[0] == '/' and str(link.get('href'))[1] != '/' and baselink + link.get('href') not in explored:
            not_explored.add(baselink + link.get('href'))
