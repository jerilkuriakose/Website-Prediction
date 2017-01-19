"""
Project Name: convertlinks
Get the actual URL from the previous result 'getlinks' project
"""

import scrapy
import json

class ConvertSpider(scrapy.Spider):
    name = "convert"

    with open('../../getlinks/links.json') as data_file:
        data = json.load(data_file)

    start_urls = list(
        set(
            [url for url in [d['link'] for d in data] if url is not None]
            )
        )

    def parse(self, response):
        yield {
            'convertedUrl': response.url.lower()
        }