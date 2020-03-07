import scrapy


class ArchSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.archlinux.org']
    start_urls = ['https://www.archlinux.org/packages/']

    def parse(self, response):
        packages = response.xpath("//td/a")
        for package in packages:
            name = package.xpath(".//text()").get()
            link = package.xpath(".//@href").get()
            arch = response.xpath('//td[1]/text()').get()

            yield response.follow(
                url=link,
                callback=self.parse_arch,
                meta={'package_name': name})

    def parse_arch(self, response):
        name = response.request.meta['package_name']
        upstream_url = response.xpath('//a[@itemprop]/@href').get()
        yield{
            'package_name': name,
            'upstream': upstream_url,
        }

# scrapy crawl test
