import scrapy
from items import MovieMetacriticItem


class ComparisonRatingSpider(scrapy.Spider):
    name = 'comparisonSpider'

    def start_requests(self):
        print('https://www.metacritic.com/movie/{}'.format(self.title))
        yield scrapy.Request('https://www.metacritic.com/movie/{}'.format(self.title))

    def parse(self, response):
        item = MovieMetacriticItem()
        item['rating'] = response.css('.metascore_w::text').extract_first()
        item['year'] = response.css('.release_year::text').extract_first()
        yield item
