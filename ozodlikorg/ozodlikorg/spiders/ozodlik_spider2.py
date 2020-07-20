import scrapy
from ..items import OzodlikorgItem

class OzodlikSpider(scrapy.Spider):
    name = 'ozodlik_2'
    # name2 = input("Search for: ")
    name2 = ''
    start_urls = [
        'https://www.polygraph.info/s?k=%s' % name2
    ]

    def parse(self, response):

        items = OzodlikorgItem()

        all_div = response.css('.fui-grid__inner')

        for media in all_div:
            title = media.css('.media-block__title--size-3::text').extract()
            content = media.css('.perex--mb::text').extract()
            author = media.css('.links__item-link::text').extract()

            items['title'] = title
            items['content'] = content
            items['author'] = author

            yield items

        next_page = response.css('li.pagination__item--next a::attr(href)').get()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
