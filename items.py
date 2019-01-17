import scrapy


class MovieImdbItem(scrapy.Item):
    plot = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    poster = scrapy.Field()
    director = scrapy.Field()
    pass


class ListItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
    id = scrapy.Field()
    poster = scrapy.Field()


class MovieMetacriticItem(scrapy.Item):
    rating = scrapy.Field()
    pass
