import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=laptops']

    def parse(self, response):
        for product in response.css('div.s-main-slot div.s-result-item'):
            yield {
                'title': product.css('h2 a span::text').get(),
                'price': product.css('span.a-price span.a-offscreen::text').get(),
                'link': product.css('h2 a::attr(href)').get(),
            }

        next_page = response.css('ul.a-pagination li.a-last a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)