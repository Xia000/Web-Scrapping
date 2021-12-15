import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    } 

baseUrl = 'https://www.mohsinnaveedranjha.com'


r = requests.get('https://www.mohsinnaveedranjha.com/unstitched-festive-21', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
productlist = soup.find_all('div', class_='item-grid')

productlinks = []

for item in productlist:
    for link in item.find_all('a', href=True):
        productlinks = list(dict.fromkeys(productlinks))
        productlinks.append(baseUrl + link['href'])

        

# for link in productlinks:
#     r = requests.get(link, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')
#     productName = soup.find('h1').text
#     print(productName)
        

r = requests.get('https://www.mohsinnaveedranjha.com/malhaar', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
images = soup.find_all('img') 

for image in images:
   
    Status = image['alt']
    if(image['alt'] == 'Sold'):      
        print(Status)
       
    

    # print(name)