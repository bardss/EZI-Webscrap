import scrapy
from items import ListItem


class ListSpider(scrapy.Spider):
    name = 'seriesSpider'

    def start_requests(self):
        yield scrapy.Request('http://www.imdb.com/find?q=%s&s=tt&ref_=fn_tt_ex' % self.query)

    def parse(self, response):
        print(response.css('.findResult'))
        for pos in response.css('.findResult'):
            print(pos)
            item = ListItem()
            item['title'] = pos.css('.result_text a::text').extract_first()
            item['year'] = pos.css('.result_text::text').re('\d+')[0]
            item['id'] = pos.css('.findResult .result_text a::attr(href)').extract()[0].split('/')[2]
            item['poster'] = pos.css('.findResult img::attr(src)').extract_first()
            yield item
