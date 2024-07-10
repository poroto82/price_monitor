import scrapy

class WalmartSpider(scrapy.Spider):
    name = 'walmart'
    allowed_domains = ['walmart.com']
    start_urls = ['https://www.walmart.com/search/?query=laptop']

    def parse(self, response):
        for product in response.css('div.search-result-gridview-item'):
            yield {
                'title': product.css('a.product-title-link span::text').get(),
                'price': product.css('span.price-main span.visuallyhidden::text').get(),
                'link': response.urljoin(product.css('a.product-title-link::attr(href)').get()),
            }

        next_page = response.css('a.paginator-btn-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)