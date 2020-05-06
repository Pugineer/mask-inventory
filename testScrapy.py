import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.hktvmall.com/hktv/zh/search_a?keyword=%E5%8F%A3%E7%BD%A9%20%20']

    def parse(self, response):
        print(1)
        response.css('.brand-product-name>h4').getall()
        for title in response.css('.brand-product-name>h4'):
            print(title)
            print("jksdghjsgkdfjkgbjkdfbjgkbkdfhgbkhdfbjgkbjkdfg")
            yield {'title': title.css('::text').get()}

        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)
