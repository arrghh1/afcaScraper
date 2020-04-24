# -*- coding: utf-8 -*-
import scrapy
from  scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['data.afca.org.au']
    start_urls = ['http://https://data.afca.org.au/banking-and-finance']

    def __init__(self):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_path = which("chromedriver")
        driver = webdriver.chrome(executable_path=chrome_path, options = chrome_options)
        driver.set_window_size(1920,1080)
        driver.get(start_urls)

        ##need to work out where to click to get started on the looping!
    
    
    def parse(self, response):
        resp = Selector(text=self.html)
        for MyElements in resp.xpath("//")
            yield{
                #things
            }
