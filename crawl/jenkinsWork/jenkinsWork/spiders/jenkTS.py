# << Swami Shreeji >> 
# @nishantpatel ; 10 Oct 2017
# To run from shell --> scrapy crawl jenkTS -a filename=test.txt

import sys
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "jenkTS"
   
    def __init__(self, filename=None):
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.readlines()

    def parse(self, response):
        yield {
        	'dependency': response.css('div.required a::text').extract(),
        }