import scrapy

class Product(scrapy.Item):
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    country = scrapy.Field()
    directions_url = scrapy.Field()
    country = scrapy.Field()
