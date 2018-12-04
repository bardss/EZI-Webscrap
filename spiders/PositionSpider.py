import scrapy
from items import MovieImdbItem


class PositionSpider(scrapy.Spider):
    name = 'positionSpider'

    def start_requests(self):
        yield scrapy.Request('http://www.imdb.com/title/%s' % self.id, callback=self.parseMovie)

    def parseMovie(self, response):
        item = MovieImdbItem()
        item['year'] = response.css('span[id=titleYear] a::text').extract_first()
        item['plot'] = response.css('div[class=summary_text]::text').extract_first()
        item['rating'] = response.css('span[itemprop=ratingValue]::text').extract_first()
        yield item
