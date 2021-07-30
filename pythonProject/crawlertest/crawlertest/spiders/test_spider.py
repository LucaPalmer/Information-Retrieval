import scrapy

class CovSpider(scrapy.Spider):
    name = "coventry"
    start_urls = [
        'https://pureportal.coventry.ac.uk/en/organisations/faculty-of-engineering-environment-computing',
    ]

    def parse(self, response):
        print("Response URL: ", response)
        link = response.xpath('//*[@id="page-content"]/div[1]/section/div/div/div/nav/ul/li[4]/a/@href')
        yield response.follow(link.get(), callback=self.parse_content)


    def parse_content(self, response):
        attributes = response.css('div.result-container')
        for attribute in attributes:
            yield{
                'Title': attribute.css('span::text').get(),
                'Non-EEC Authors': attribute.css('div.rendering::text')[0:1].get(),
                'EEC Authors': attribute.xpath('.//*[@class="link person"]/span/text()').get(),
                'Type': attribute.css('span.type_classification_parent::text').get(),
                'Year': attribute.css('span.date::text').re(r'\d{4}'), # Convert to String
                'EEC Author Profile': attribute.css('a.link.person::attr(href)').get(),
                'Paper Profile': attribute.css('a.link::attr(href)').get(),
                            }
            next_page = response.xpath('//*[@id="main-content"]/div/section/nav/ul/li[13]/a/@href').get()
            if next_page is not None:
                next_page_link = response.urljoin(next_page)
                yield response.follow(url=next_page_link, callback=self.parse_content)

