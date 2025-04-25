import scrapy


class QuotesScraperSpider(scrapy.Spider):
    name = "quotes_scraper"
    allowed_domains = ["quotes.toscrape.com"]

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS': 1,
        'FEED_URI': 'output/quotes.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'LOG_LEVEL': 'INFO'
    }

    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        self.logger.info("Scraping page: %s", response.url)
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            yield {
                'text': text,
                'author': author,
                'tags': tags
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
