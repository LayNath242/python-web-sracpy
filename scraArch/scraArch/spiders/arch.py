# -*- coding: utf-8 -*-
import scrapy


class ArchSpider(scrapy.Spider):
    name = 'arch'
    allowed_domains = ['www.archlinux.org/packages/']
    start_urls = ['http://www.archlinux.org/packages/']

    def parse(self, response):
        packages = response.xpath('//td/a')
        for package in packages:
            name = package.xpath('.//text()').get()
            link = package.xpath('.//@href').get()

            yield{
                'package_name': name,
                'package_link': link,
            }
