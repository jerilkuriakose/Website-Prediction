"""
Get URLs of some popular e-Commerce websites - www.digit.in

For more information about the scrapped URL, see
http://www.digit.in/technology-guides/fasttrack-to-e-commerce/top-50-e-commerce-websites-in-india.html
"""

from bs4 import BeautifulSoup
import requests
import csv
import re

# URL that is to be scrapped
url = 'http://www.digit.in/technology-guides/fasttrack-to-e-commerce/top-50-e-commerce-websites-in-india.html'
# Adding User-Agent
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"}
# For concatenating with the fetched URL
start = 'http://www.'
# Pattern to get the URL from page
regex = ur'\s(.+?\.com)'

# To disable proxy setting
try:
	response = session.get(url, headers=header)
except:
	session = requests.Session()
	session.trust_env = False
	response = session.get(url, headers=header)

# Reading the contents of the page
soup = BeautifulSoup(response.content, 'lxml')
data = soup.find_all('strong')

# Getting only the required 'href'
links = [re.findall(regex, d.text)[0].lower() for d in data if re.findall(regex, d.text)]

# Saving as '.csv' file
with open('data/digit.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    for link in links:
        wr.writerow([start + link.lower()])