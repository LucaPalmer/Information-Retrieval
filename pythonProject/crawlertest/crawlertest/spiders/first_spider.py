import scrapy


class firstSpider(scrapy.Spider):
    name = "first"
    allowed_domains = ["pureportal.coventry.ac.uk/"]

    start_urls = [
        "https://pureportal.coventry.ac.uk/en/organisations/faculty-of-engineering-environment-computing"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)