"""
Get URLs of some popular e-Commerce websites - www.iimnet.com

For more information about the scrapped URL, see
http://www.iimnet.com/profiles/blogs/list-of-e-commerce-companies-in-india
"""

from bs4 import BeautifulSoup
import requests
import csv

# URL that is to be scrapped
url = 'http://www.iimnet.com/profiles/blogs/list-of-e-commerce-companies-in-india'
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
links = [a['href'] for a in soup.find_all('a', {'target': '_blank'}, href=True)][3:185]

# Saving as '.csv' file
with open('data/iimnet.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    for link in links:
        wr.writerow([link.lower()])