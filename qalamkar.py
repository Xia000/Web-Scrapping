import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime




baseURL = 'https://www.qalamkar.com.pk'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }    

r = requests.get('https://www.qalamkar.com.pk/collections/winter-shawl-collection')
soup = BeautifulSoup(r.content, 'lxml')
productsList = soup.find_all('div', class_='product-collection products-grid row')

productLinks = []
headerList = ['Name', 'Inventory', 'Image Link','Link' ]

for item in productsList:
    for link in item.find_all('a', href=True, class_='product-title'):
        productLinks.append( baseURL + link['href'])




# testLinks = 'https://www.qalamkar.com.pk/collections/winter-shawl-collection/products/kk-02'

for link in productLinks:

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    productName = soup.find('h2', itemprop ='name').text.strip()
    # imageLink =  soup.find('img' , id='product-featured-image-31801554665647') 
    imageLink = soup.find('a', href=True , class_='fancybox')
    finalImageLink = 'https' + imageLink['href']
    # fullImageLink =  imageLink['src']

    # status = soup.find('strong', class_='sold-out-label').text.strip()
    statusValue = soup.find('input', attrs={'name': 'add'})
    finalstatusValue = statusValue['value']
    # print( 'https:' + imageLink['src'])

    # print(productName , status, 'https:' + imageLink['src'])

    product = {
        'ProductLink': link,
        'name': productName,
        'Stock' : finalstatusValue,
        # 'status': status,
        'image': finalImageLink
    }
    
    print('Processing')
    df = pd.DataFrame(product, index=[0])   
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


