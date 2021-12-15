import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    } 

baseUrl = 'https://www.asimjofa.com'


r = requests.get(f'https://www.asimjofa.com/chiffon-collection#/pageSize=18&viewMode=grid&orderBy=0', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
productlist = soup.find_all('div', class_='item-grid')


productlinks = []

for item in productlist:
    for link in item.find_all('a', href=True):
        productlinks = list(dict.fromkeys(productlinks))
        productlinks.append(baseUrl + link['href'])
        
            
print(len(productlinks))
exit()  
testLink = 'https://www.asimjofa.com/ajn-11'
i = 758

# 'add-to-cart-button-796'
for link in productlinks:

    inputLink = 'add-to-cart-button-'+str(i)
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    productName = soup.find('h1').text
    status =  soup.find('input', {'id':inputLink}).attrs['value']
    print(inputLink)
    i += 1
    if(i== 765):
        break
    # i += 1
    # if(i== 770):
    #     break
    data = {
        'name': productName,
        'link': link,
        'Status': status
    }

    print(data) 