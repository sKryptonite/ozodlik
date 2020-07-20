import scrapy
from ..items import OzodlikorgItem

class OzodlikSpider(scrapy.Spider):
    name = 'rus_ozodlik'
    def __init__(self, *a, **kw):
        super(OzodlikSpider, self).__init__(*a, **kw)
        self.name2 = kw.get('name2')
        self.start_urls = ['https://rus.ozodlik.org/s?k=%s' % self.name2]

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