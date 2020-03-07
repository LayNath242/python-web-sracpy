# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        n = 1
        countries = response.xpath('//td/a')
        for country in countries:
            name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()
            n += 1
            # yield{
            #     'country_name': name,
            #     'country_link': link,
            #     'new_link': response.follow(url=link),
            #     'n': n
            # }
            new_link = f"https://www.worldometers.info{link}"
            yield scrapy.Request(new_link)


# scrapy crawl countries
