from bs4 import BeautifulSoup
import requests

page = requests.get('https://es.wikipedia.org/wiki/Python')
soup = BeautifulSoup(page.content,'html.parser')

content = soup.find('body').find_all('p') 

import re
def clean_html(html):
    expression = re.compile('<.*?>')
    return re.sub(expression,'',html)


for element in content:
    print(clean_html(str(element)))
