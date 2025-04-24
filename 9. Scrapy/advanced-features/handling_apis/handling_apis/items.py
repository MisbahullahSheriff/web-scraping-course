import scrapy


class ApiScraperItem(scrapy.Item):
    userId = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
