1. install scrapy
   pipenv install scrapy

2. scrapy startproject < your projectname >

3. > scrapy genspider < filename > <url>
   > ex: www.worldometers.info/world-population/population-by-country
   > scrapy genspider -t crawl < filename > <url>

4. goto < filename > in spiders directory

    whatUwant = response.xpath('//??/text()').get()
    whatUwant = response.xpath('//??/text()').getall() // list of data

5. goto terminal and run: scrapy crawl < filename >

6. to save dataset

    scrapy crawl <filename> -o <name.json>
