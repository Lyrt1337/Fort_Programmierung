import scrapy

class EventspiderSpider(scrapy.Spider):
    name = "eventspider"
    allowed_domains = ["chur.ch"]
    start_urls = ["https://www.chur.ch/anlaesseaktuelles?ort="]

    def parse(self, response):
        pass
