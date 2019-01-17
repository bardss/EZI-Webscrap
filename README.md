# EZI-Webscrap
IMBD Python Webscrapper 

## Server IP:

    http://13.81.106.52/


## Endpoints:

    @route("/search/<query>")
  
    @route("/title/<id>")
  
    @route("/metacritic-rating/<title>")
  
  
## DTO: (all fields are strings)

    class MovieImdbItem(scrapy.Item):

      plot = scrapy.Field()
    
      year = scrapy.Field()
    
      rating = scrapy.Field()


    class ListItem(scrapy.Item):

      title = scrapy.Field()
    
      year = scrapy.Field()
    
      id = scrapy.Field()


    class MovieMetacriticItem(scrapy.Item):

      rating = scrapy.Field()
