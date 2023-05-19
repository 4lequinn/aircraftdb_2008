from bs4 import BeautifulSoup
import requests

page = requests.get('https://es.wikipedia.org/wiki/Python')
soup = BeautifulSoup(page.content,'html.parser')

# title
#print(soup.title)

# Parent
#print(soup.title.parent)

# Content
#print(soup.prettify())

#print(soup.children)

# extract data
for child in soup.title.children: pass
    #print(child)

# a links

# First ocurrence
#print(soup.a)

links = soup.find_all('a')
#print(links)

links = soup.find('a')
#print(links.find_next())


print(links.contents)

print(links.text)