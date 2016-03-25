import scrapy

class Job(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.field()
    description = scrapy.field()
    email = scrapy.field()
