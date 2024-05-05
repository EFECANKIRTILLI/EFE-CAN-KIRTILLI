# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GamesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_name = scrapy.Field()
    game_year = scrapy.Field()
    game_type = scrapy.Field()
    game_rate = scrapy.Field()
    game_intro = scrapy.Field()
    game_votes = scrapy.Field()

    pass
