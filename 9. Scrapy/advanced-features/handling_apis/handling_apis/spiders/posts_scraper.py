import scrapy
from handling_apis.items import ApiScraperItem


class PostsScraperSpider(scrapy.Spider):
    name = "posts_scraper"
    allowed_domains = ["jsonplaceholder.typicode.com"]
    # start_urls = ["https://jsonplaceholder.typicode.com/posts"]

    def start_requests(self):
        yield scrapy.Request(
            url='https://jsonplaceholder.typicode.com/posts',
            headers={'User-Agent': 'Mozilla/5.0'},
            callback=self.parse
        )

    def parse(self, response):
        data = response.json()
        for post in data:
            item = ApiScraperItem()
            item['userId'] = post['userId']
            item['id'] = post['id']
            item['title'] = post['title']
            item['body'] = post['body']
            yield item
