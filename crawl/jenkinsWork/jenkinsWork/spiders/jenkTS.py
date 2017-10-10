# << Swami Shreeji >> 
# @nishantpatel ; 10 Oct 2017 response.css('div.required a::text').extract()

import sys
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "jenkTS"
    start_urls = [
        'https://plugins.jenkins.io/android-lint',
    ]

    def parse(self, response):
        yield {
        	'dependency': response.css('div.required a::text').extract(),
        }