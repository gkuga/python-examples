import scrapy


class ScrapinghubSpider(scrapy.Spider):
    name = "scrapinghub"
    allowed_domains = ["blog.scrapinghub.com"]
    start_urls = ["https://blog.scrapinghub.com"]

    def parse(self, response):
        pass
