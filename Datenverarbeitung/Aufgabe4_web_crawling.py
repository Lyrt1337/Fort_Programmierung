import scrapy
from scrapy.crawler import CrawlerProcess

class EventSpider(scrapy.Spider):
    name = "event-spider"
    # start_urls = ["https://www.zyte.com/blog/"]
    start_urls = ["https://www.chur.ch/anlaesseaktuelles?ort="]

    def parse(self, response):
        for row in response.xpath('//*[@class="table icms-dt rs_preserve dataTable no-footer dtr-inline"]//tbody//tr'):
            yield {"Date": row.xpath('td[1]//text()').extract(),
                   "title": row.xpath('td[2]//text()').extract()}
    # def parse(self, response):
    #     for title in response.css("div.col-sm-12.table"):
    #         yield {"Date": title.css("td.span.text-nowrap::text"),
    #                "title": title.css("td.icms-datatable-col-name::text").get()}
    #
    #     for next_page in response.css("a.next"):
    #         yield response.follow(next_page, self.parse)


# run spider
process = CrawlerProcess(settings={
    "FEEDS": {
        "output2.json": {"format": "json"},
    },
})
process.crawl(EventSpider)
process.start()

# <a href="/_rte/anlass/5394008">Ausstellung Ilse Weber. Helle Nacht</a>
# Ausstellung Ilse Weber. Helle Nacht