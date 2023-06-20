import scrapy
from scrapy.crawler import CrawlerProcess


class EventSpider(scrapy.Spider):
    name = "eventspider"
    start_urls = ["https://www.chur.ch/anlaesseaktuelles?ort="]

    def parse(self, response):
        # Finde alle Event-Einträge auf der Seite

        # events = response.css(".event-list-item")
        events = response.css("div.content-inner")

        for event in events:
            # Extrahiere die relevanten Informationen
            title = event.css(".name a::text").get()
            date = event.css(".span.d-none d-md-block::text").get()
            location = event.css(".organisator::text").get()
            # title = event.css(".title a::text").get()
            # date = event.css(".date::text").get()
            # location = event.css(".location::text").get()

            # Drucke die Informationen (kann an deine Bedürfnisse angepasst werden)
            print("Titel:", title)
            print("Datum:", date)
            print("Ort:", location)
            print("-----")

        # Folge dem Link zur nächsten Seite (falls vorhanden)
        next_page_url = response.css(".pagination-next a::attr(href)").get()
        if next_page_url:
            yield response.follow(next_page_url, self.parse)


process = CrawlerProcess(settings={
    "FEEDS": {
        "output3.json": {"format": "json"},
    },
})
process.crawl(EventSpider)
process.start()

#
"""
untersuchen > rechtsklick auf element im html > kopieren als "CSS-Selector"


.contentTitle

#anlassList > tbody:nth-child(2)

response.css("#anlassList")
response.xpath('//*[@id="anlassList"]')
tr.odd:nth-child(1) > td:nth-child(1) > span:nth-child(1)
#anlassList
.icms-wysiwyg-table
html body.anlaesseaktuelles div.main-outercon div.content-outer div.container div.content-inner div.row div.col-center.col-sm-9 div.box div#maincontent.container-fluid.box2 div.row div.icms-content-col-a div.row div.icms-global-table-container div#anlassList_wrapper.dataTables_wrapper.dt-bootstrap4.no-footer div.row div.col-sm-12 table#anlassList.table.icms-dt.rs_preserve.dataTable.no-footer.dtr-inline

"""