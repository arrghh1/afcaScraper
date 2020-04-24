# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['https://data.afca.org.au/banking-and-finance/']
    start_urls = ['http://https://data.afca.org.au/banking-and-finance//']

    def parse(self, response):
        pass
