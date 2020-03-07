# -*- coding: utf-8 -*-
import scrapy


class ArchSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.archlinux.org']
    start_urls = ['https://www.archlinux.org/packages/']

    def parse(self, response):
        packages = response.xpath('//tr')
        for package in packages:
            arch = package.xpath('.//td[1]/text()').get()
            repo = package.xpath('.//td[2]/text()').get()
            name = package.xpath('.//td[3]/a/text()').get()
            link = package.xpath('.//td[3]/a/@href').get()
            desc = package.xpath('.//td[5]/text()').get()

            link = f'https://www.archlinux.org{link}'
            yield scrapy.Request(
                url=link, callback=self.parse_arch,
                meta={'package_name': name,
                      'arch': arch,
                      'repo': repo,
                      'desc': desc,
                      })

    def parse_arch(self, response):
        name = response.request.meta['package_name']
        arch = response.request.meta['arch']
        repo = response.request.meta['repo']
        desc = response.request.meta['desc']
        upstream_url = response.xpath('//a[@itemprop]/@href').get()
        yield{
            'architecture': arch,
            'repository:': repo,
            'package_name': name,
            'upstream': upstream_url,
            'description': desc,
        }


#  scrapy crawl test
