# -*- coding: utf-8 -*-
import scrapy
from  scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['data.afca.org.au']
    start_urls = ['https://data.afca.org.au/banking-and-finance']

    
    def __init__(self):
        #chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(executable_path=chrome_path) #, options = chrome_options)
        driver.set_window_size(1920,1080)
        driver.get('https://data.afca.org.au/banking-and-finance')
        try:
            WebDriverWait(driver,100).until(EC.presence_of_element_located((By.CLASS_NAME, "tableExContainer")))
            self.html = driver.page_source
        ##need to work out where to click to get started on the looping!
        finally:
            driver.quit()
    
    def parse(self, response):
        resp = Selector(text=self.html)
        for MyElements in resp.xpath("//div[@class='tableEx']"):
            yield {
                'thing':(MyElements)
                 }
