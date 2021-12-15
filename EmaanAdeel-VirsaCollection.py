from typing import SupportsComplex
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    } 

baseUrl = 'https://emaanadeel.com'


r = requests.get('https://emaanadeel.com/collections/virsa-collection', headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
productlist = soup.find_all('div', class_='grid grid--uniform grid--collection')


productlinks = []

for item in productlist:
    for link in item.find_all('a', class_='grid-product__link', href=True):
        productlinks = list(dict.fromkeys(productlinks))
        productlinks.append(baseUrl + link['href'])


for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    productName = soup.find('h1', class_='h2 product-single__title').text.strip()
    status = soup.find('button', class_='btn btn--full add-to-cart').text.strip()
    

    data = {
        'Product Name': productName,
        'Status': status,
        'Link': link
    }
    print('Processing')    
    df = pd.DataFrame(data, index=[0])   
    df.to_csv('products.csv', mode='a', header=False, index=False)