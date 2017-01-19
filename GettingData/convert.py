"""
Converting the URLs from JSON format to CSV
"""

import json
import csv

# Read the JSON file
with open('convertlinks/convert.json') as data_file:
        data = json.load(data_file)

# Get the required links
links = [d['convertedUrl'] for d in data]

# Saving as '.csv' file
with open('data/converted.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    for link in links:
        wr.writerow([link.lower()])