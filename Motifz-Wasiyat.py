import requests
from bs4 import BeautifulSoup
import pandas as pd

from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    } 

baseUrl = 'https://www.motifz.com.pk'

r = requests.get('https://www.motifz.com.pk/collections/mehrunisa-cotton-satin', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
productlist = soup.find_all('div', class_='category-products')

# print(productlist)
productlinks = []

for item in productlist:
    for link in item.find_all('a', class_='product-image', href=True):
        productlinks.append(baseUrl + link.get('href'))



for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    productname = soup.find('div', class_='product-name top-product-detail').text.strip()
    status = soup.find('button', class_='btn-cart add-to-cart bordered uppercase').text.strip()

    # print(productname,status,testlink)

    data = {
        'productname': productname,
        'status': status,
        'link': link,
    }

    print('Fetching the Product Data')
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

