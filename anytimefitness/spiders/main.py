import scrapy
# from anytimefitness.items import Product
from lxml import html

class AnytimefitnessSpider(scrapy.Spider):
    name = "anytimefitness"
    start_urls = ["https://example.com"]

    def parse(self, response):
        parser = html.fromstring(response.text)
        print("Visited:", response.url)
