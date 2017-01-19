"""
Project Name: gettitle
Get the actual URL from the previous result 'getlinks' project
"""

import scrapy
import csv

class TitleSpider(scrapy.Spider):
    name = "titles"
    with open('../websites.txt') as data_file:
        links = list(csv.reader(data_file))

    start_urls = ['http://www.' + url for link in links for url in link]

    def parse(self, response):
        yield {
            'url': response.url,
            'title': response.css('title::text').extract_first(),
        }