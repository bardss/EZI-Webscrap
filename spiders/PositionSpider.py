import scrapy
from items import MovieItem


class PositionSpider(scrapy.Spider):
    name = 'positionSpider'

    def start_requests(self):
        yield scrapy.Request('http://www.imdb.com/title/%s' % self.id, callback=self.parseMovie)

    def parseMovie(self, response):
        item = MovieItem()
        item['title'] = response.css('h1[itemprop=name]::text').extract_first()
        item['year'] = response.css('span[id=titleYear] a::text').extract_first()
        item['plot'] = response.css('[itemprop=description] p::text').extract_first()
        yield item
