"""
Get URLs of some popular e-Commerce websites - www.paulnrogers.com

For more information about the scrapped URL, see
https://paulnrogers.com/top-50-ecommerce-websites/
"""

from bs4 import BeautifulSoup
import requests
import csv

# URL that is to be scrapped
url = 'https://paulnrogers.com/top-50-ecommerce-websites/'
# Adding User-Agent
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"}

# To disable proxy setting
try:
	response = session.get(url, headers=header)
except:
	session = requests.Session()
	session.trust_env = False
	response = session.get(url, headers=header)

# Reading the contents of the page
soup = BeautifulSoup(response.content, 'lxml')

# Getting only the required 'href'
links = [a['href'] for t in soup.find_all('p', {'style': 'text-align: center;'}) for a in t.find_all('a', href=True)]

# Saving as '.csv' file
with open('data/paulnrogers.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    for link in links:
        wr.writerow([link.lower()])