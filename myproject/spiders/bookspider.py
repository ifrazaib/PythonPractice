import scrapy

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')

        if not books:
            self.logger.error("No books found on the page!")

        for book in books:
            item = {
                'name': book.css('h3 a::attr(title)').get(),
                'price': book.css('.product_price .price_color::text').get(),
                'url': response.urljoin(book.css('h3 a::attr(href)').get()),
            }
            self.logger.info(f"Scraped item: {item}")
            yield item
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
           ## if 'catalogue/' in next_page:
              ## next_page_url =  'https://books.toscrape.com' + next_page
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)

        else:
            next_page_url =  'https://books.toscrape.com/catalogue/' + next_page
        yield response.follow(next_page_url,callback = self.parse)

