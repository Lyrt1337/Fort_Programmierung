import scrapy


class BasicspiderSpider(scrapy.Spider):
    name = "basicSpider"
    allowed_domains = ["localhost"]
    start_urls = ["http://localhost:8000/"]

    def parse(self, response):
        yield {"url": response.url, "title": response.css("title::text").get()}

        for a in response.css("a[href]"):
            yield response.follow(a, self.parse)
