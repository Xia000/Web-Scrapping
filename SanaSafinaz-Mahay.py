import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    } 

baseUrl = 'https://www.sanasafinaz.com'


r = requests.get('https://www.sanasafinaz.com/pk/unstitched-fabric/mahay-summer-21.html', headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
productlist = soup.find_all('ol', class_='products list items product-items')

productlinks = []

for item in productlist:
    for link in item.find_all('a', class_='product photo product-item-photo sl-product-item-photo', href=True):
        # productlinks = list(dict.fromkeys(productlinks))
        productlinks.append(link['href'])
        # print(link['href'])


# testlink = 'https://www.sanasafinaz.com/pk/l211-006b-cl-l211-006b-cl.html'

for link in productlinks:
    r = requests.get(link , headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    productName = soup.find('span', class_='base').text.strip()

    try:
        stock_available = soup.find('div' , class_= 'stock available').text
    except:
        stock_available = 'Out of Stock'

    # print(productName, stock_available, link)
    data = {
        'productName': productName,
        'stock_available': stock_available,
        'link': link
        }
    print(data) 
    
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


