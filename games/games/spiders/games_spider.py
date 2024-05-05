import scrapy
from ..items import GamesItem


class GamesSpiderSpider(scrapy.Spider):
    name = "games"
    start_urls = ["https://www.imdb.com/list/ls027813592/"]

    def parse(self, response):
        for game in response.css('.lister-item'):
            items = GamesItem()
            game_name = game.css('.lister-item-header a::text').get()
            game_year = game.css('.lister-item-year::text').get()
            game_type = game.css('.genre::text').get()
            game_rate = game.css('.ipl-rating-star.small .ipl-rating-star__rating::text').get()
            game_intro = game.css('.ratings-bar+ p::text').get()
            game_votes = game.css('.list-description::text').get()

            items['game_name'] = game_name.strip() if game_name else None
            items['game_year'] = game_year.strip() if game_year else None
            items['game_type'] = game_type.strip() if game_type else None
            items['game_rate'] = game_rate.strip() if game_rate else None
            items['game_intro'] = game_intro.strip() if game_intro else None
            items['game_votes'] = game_votes.strip() if game_votes else None

            yield items

