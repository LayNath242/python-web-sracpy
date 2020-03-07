# -*- coding: utf-8 -*-
import scrapy


class ArchSpider(scrapy.Spider):
    name = 'arch'
    allowed_domains = ['www.archlinux.org']
    start_urls = ['https://www.archlinux.org/packages/']

    def parse(self, response):
        packages = response.xpath('//tr')
        for package in packages:
            arch = package.xpath('.//td[1]/text()').get()
            repo = package.xpath('.//td[2]/text()').get()
            name = package.xpath('.//td[3]/a/text()').get()
            link = package.xpath('.//td[3]/a/@href').get()
            Description = package.xpath('.//td[5]/text()').get()

            link = f'https://www.archlinux.org{link}'
            yield scrapy.Request(
                url=link, callback=self.parse_arch,
                meta={'package_name': name,
                      'arch': arch,
                      'repo': repo,
                      'Description': Description,
                      })

            # yield{
            #     'arch': arch,
            #     'repo': repo,
            #     'package_name': name,
            #     # 'upstream': upstream_url,
            #     'Description': Description,
            # }

        next_page = response.xpath("(//span/a/@href)[2]").get()
        next_page = f'https://www.archlinux.org/packages/{next_page}'
        if next_page:
            yield scrapy.Request(url=next_page,
                                 callback=self.parse,
                                 )

    def parse_arch(self, response):
        name = response.request.meta['package_name']
        arch = response.request.meta['arch']
        repo = response.request.meta['repo']
        Description = response.request.meta['Description']
        upstream_url = response.xpath('//a[@itemprop]/@href').get()
        yield{
            'arch': arch,
            'repo': repo,
            'package_name': name,
            'upstream': upstream_url,
            'Description': Description,
        }


#  scrapy crawl arch -o archLinux.json
