"""
Project Name: getlinks
Get URLs of some popular e-Commerce websites - www.thetoptens.com

For more information about the scrapped URL, see
http://www.thetoptens.com/ecommerce-websites-india/
"""

import scrapy

class LinksSpider(scrapy.Spider):
    name = "links"
    start_urls = [
        'http://www.thetoptens.com/ecommerce-websites-india/',
    ]

    def parse(self, response):
        for quote in response.css('div.i'):
            yield {
                'link': quote.css('a::attr(href)').extract_first(),
                'description': quote.css('p::text').extract()
            }

        
        next_page = response.css('div.pages a.g::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)