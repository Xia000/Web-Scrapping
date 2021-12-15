import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


baseURL = 'https://www.houseofcharizma.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }    

r = requests.get('https://www.houseofcharizma.com/collections/unstitched-embroidered-naranji')
soup = BeautifulSoup(r.content, 'lxml')
productsList = soup.find_all('div', class_='product-collection products-grid row')


productlinks = []


for item in productsList:
    for link in item.find_all('a', href=True, class_='product-title'):
        productlinks = list(dict.fromkeys(productlinks))
        productlinks.append( baseURL + link['href'])

testlink = 'https://www.houseofcharizma.com/collections/unstitched-embroidered-naranji/products/3-pc-unstitched-embroidered-khaddar-cnw-10'

for link in productlinks:
    r = requests.get(link, headers=headers)
    # r = requests.get(testlink, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    productName = soup.find('span').text.strip()
    status = soup.find('input', id='product-add-to-cart').get('value')

    data = {
        'productName': productName,
        'status': status,
        'link': link,
    }

    print('Processing')    
    df = pd.DataFrame(data, index=[0])   
    df.to_csv('products.csv', mode='a', header=False, index=False)

    # Pre-requisite - Import the writer class from the csv module
from csv import writer

# The data assigned to the list 
currrent_data = datetime.now()
list_data=[ currrent_data , currrent_data ,currrent_data ,currrent_data]

# Pre-requisite - The CSV file should be manually closed before running this code.

# First, open the old CSV file in append mode, hence mentioned as 'a'
# Then, for the CSV file, create a file object
with open('products.csv', 'a', newline='') as f_object:  
    # Pass the CSV  file object to the writer() function
    writer_object = writer(f_object)
    # Result - a writer object
    # Pass the data in the list as an argument into the writerow() function
    writer_object.writerow(list_data)  
    # Close the file object
    f_object.close()

