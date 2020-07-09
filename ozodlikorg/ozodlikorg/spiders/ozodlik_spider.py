import scrapy
from ..items import OzodlikorgItem

class OzodlikSpider(scrapy.Spider):
    name = 'ozodlik'
    name2 = input("Search for: ")
    start_urls = [
        'https://www.rferl.org/s?k=%s' % name2,
        'https://www.polygraph.info/s?k=%s' % name2,
        'https://pressroom.rferl.org/s?k=%s' % name2,
        'https://www.currenttime.tv/s?k=%s' % name2,
        # 'https://www.currenttime.tv/tv',
        'https://en.currenttime.tv/s?k=%s' % name2,
        'https: // www.svaboda.org/s?k=%s' % name2,
        # 'https: // www.svaboda.org / radio',
        'https://www.radiosvoboda.org/s?k=%s' % name2,
        # 'https: // www.radiosvoboda.org / radio',
        'https://ktat.krymr.com/s?k=%s' % name2,
        'https://ua.krymr.com/s?k=%s' % name2,
        # 'https: // ua.krymr.com / radio',
        'https://ru.krymr.com/s?k=%s' % name2,
        # 'https: // ru.krymr.com / radio',
        'https://moldova.europalibera.org/s?k=%s' % name2,
        # 'https: // moldova.europalibera.org / radio',
        'https://romania.europalibera.org/s?k=%s' % name2,
        'https://www.svobodnaevropa.bg/s?k=%s' % name2,
        'https://www.slobodnaevropa.org/s?k=%s' % name2,
        # 'https: // www.slobodnaevropa.org / radio',
        'https://www.slobodnaevropa.mk/s?k=%s' % name2,
        # 'https: // www.slobodnaevropa.mk / radio',
        'https://www.evropaelire.org/s?k=%s' % name2,
        # 'https: // www.evropaelire.org / radio',
        'https://www.svoboda.org/s?k=%s' % name2,
        # 'https: // www.svoboda.org / radio',
        # 'https: // www.svoboda.org / tv',
        'https://www.severreal.org/s?k=%s' % name2,
        'https://www.sibreal.org/s?k=%s' % name2,
        'https://www.factograph.info/s?k=%s' % name2,
        'https://www.azatliq.org/s?k=%s' % name2,
        'https://www.idelreal.org/s?k=%s' % name2,
        'https://www.kavkazr.com/s?k=%s' % name2,
        'https://www.radiomarsho.com/s?k=%s' % name2,
        'https://www.azatutyun.am/s?k=%s' % name2,
        # 'https: // www.azatutyun.am / radio',
        'https://rus.azatutyun.am/s?k=%s' % name2,
        'https://www.azadliq.org/s?k=%s' % name2,
        # 'https: // www.azadliq.org / radio',
        'https://www.radiotavisupleba.ge/s?k=%s' % name2,
        # 'https: // www.radiotavisupleba.ge / radio',
        'https://www.ekhokavkaza.com/s?k=%s' % name2,
        # 'https: // www.ekhokavkaza.com / radio',
        'https://www.radiofarda.com/s?k=%s' % name2,
        # 'https: // www.radiofarda.com / radio',
        # 'https: // www.radiofarda.com / tv',
        'https://en.radiofarda.com/s?k=%s' % name2,
        'https://www.azattyq.org/s?k=%s' % name2,
        'https://rus.azattyq.org/s?k=%s' % name2,
        'https://www.azattyk.org/s?k=%s' % name2,
        # 'https: // www.azattyk.org / radio',
        # 'https: // www.azattyk.org / tv',
        'https://rus.azattyk.org/s?k=%s' % name2,
        # 'https: // rus.azattyk.org / radio',
        'https://www.ozodi.org/s?k=%s' % name2,
        # 'https: // www.ozodi.org / radio',
        # 'https: // www.ozodi.org / tv',
        'https://rus.ozodi.org/s?k=%s' % name2,
        'https://www.azathabar.com/s?k=%s' % name2,
        # 'https: // www.azathabar.com / radio',
        'https://rus.azathabar.com/s?k=%s' % name2,
        'https://www.ozodlik.org/s?k=%s' % name2,
        # 'https: // www.ozodlik.org / radio',
        'https://rus.ozodlik.org/s?k=%s' % name2,
        'https://pa.azadiradio.com/s?k=%s' % name2,
        # 'https: // pa.azadiradio.com / radio',
        'https://da.azadiradio.com/s?k=%s' % name2,
        # 'https: // da.azadiradio.com / radio',
        'https://gandhara.rferl.org/s?k=%s' % name2,
        'https://www.mashaalradio.com/s?k=%s' % name2,
        # 'https: // www.mashaalradio.com / radio',

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
