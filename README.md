# afcaScraper
Australian Financial Complaints Authority  Power BI Scraper.

Using Python, Scrapy, and Selenium. The intent was originally to take the XHR message from powerBI for the table views specifically, and use that, but there is some kind of dark magic making this a particularly difficult problem (happy to chat to anyone about this!) Instead, I'll use selenium, and pull out the div's for the table, and hope that order is somehow achievable from this.

Note: Key components missing: `chromedriver.exe` no point backing that to github, so if you need to run this, you'll need to install that.
Also:
    `pip install selenium`
    `pip install scrapy-selenium`
