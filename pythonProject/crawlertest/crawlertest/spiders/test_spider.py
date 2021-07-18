import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'https://pureportal.coventry.ac.uk/en/organisations/faculty-of-engineering-environment-computing',
    ]

    def parse(self, response):
        for link in response.xpath('//*[@id="page-content"]/div[1]/section/div/div/div/nav/ul/li[4]/a/@href'):
            yield response.follow(link.get(), callback=self.parse_titles)


    def parse_titles(self, response):
        attributes = response.css('div.result-container')
        for attribute in attributes:
            yield{
                'Title': attribute.css('span::text').get(),
                'Non-EEC Authors': attribute.css('div.rendering::text')[0:1].extract(),
                'EEC Authors': attribute.xpath('.//*[@class="link person"]/span/text()').extract(),
                'Type': attribute.css('span.type_classification_parent::text').get(),
                'Year': attribute.css('span.date::text').re(r'\d{4}'),
                'EEC Author Profile': attribute.css('a.link.person::attr(href)').get(),
                'Paper Profile': attribute.css('a.link::attr(href)').get(),
                            }

# response.xpath('//*[@id="main-content"]/div/section/ul/li[1]/div[2]/div[1]/text()[1]'), #gets
# attributes.xpath('descendant-or-self::text()')[3].get(),
# attribute.xpath('//*[@id="main-content"]/div/section/ul/li[1]/div[2]/div[1]/text()')[0:2].getall()
# THIS ONE: response.css('div.rendering::text').getall()
#attribute.css('div.rendering::text, a.link.person::attr(href)').get()
# response.xpath('/html/body/main/div[1]/div/div/section/ul/li/div/div/text()').getall()
# response.xpath('/html/body/main/div[1]/div/div/section/ul/li/div/div/text()').re('[A-Za-z]+') # get all names


