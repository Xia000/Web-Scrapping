import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'       
    }

baseUrl = 'https://rangrasiya.com.pk'


r = requests.get('https://rangrasiya.com.pk/collections/winter-premium-collection-21', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
productsList = soup.find_all('div', class_='grid grid--uniform grid--collection')

productLinks = []

for item in productsList:
    for link in item.find_all('a'):
        productLinks.append(baseUrl + link.get('href'))
        # print(baseUrl + link.get('href'))
print(len(productLinks))
id = [  'AddToCartText-7433838756053',
        'AddToCartText-7433848258773',
        'AddToCartText-7433824927957',
        'AddToCartText-7433844916437',
        'AddToCartText-7433837510869',
        'AddToCartText-7433822372053',
        'AddToCartText-7433849733333',
        'AddToCartText-7433853796565',
        'AddToCartText-7433827647701',
        'AddToCartText-7433830826197',
        'AddToCartText-7433850945749',
        'AddToCartText-7433819422933',
        'AddToCartText-7433852125397',
        'AddToCartText-7433849079069',
        'AddToCartText-7433855041749',
        'AddToCartText-7433829155029',
         ]


testlink = 'https://rangrasiya.com.pk/collections/winter-premium-collection-21/products/arezou'
i = 0


for link in productLinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml') 
    status = soup.find('span', id=id[i]).text.strip()
    # print(id[i])
    # print(i)
    print(status)
    # if(i > 15):
    #  print('Brek the loop')
    #  break
    i = i + 1
    print(i)
    # status = soup.find('span', id=id[i]).text.strip()
    # print(status)
    # 
    
   



