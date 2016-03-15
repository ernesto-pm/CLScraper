# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor

class CraigspiderSpider(CrawlSpider):
    name = "CraigSpider"
    allowed_domains = ["losangeles.craigslist.org"]
    start_urls = ["http://losangeles.craigslist.org/search/cpg?query=web&is_paid=all"]
    #start_urls = ["http://losangeles.craigslist.org/search/cpg"]
    #start_urls = ["http://losangeles.craigslist.org/search/cpg?query=web&is_paid=all&srchType=T"]


    #rules = (Rule(LinkExtractor(allow=(r'.*?/.+?/cpg/\d+\.html')), callback='parse_page', follow=False),)
    rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_page", follow= True),)

    def parse_start_url(self, response):
        return self.parse_page(response)

    def parse_page(self, response):
        items = response.selector.xpath("//p[@class='row']")
        #print(len(items))
        for i in items:
            link = i.xpath("./span[@class='txt']/span[@class='pl']/a/@href").extract()
            #la clase cambia en los siguientes resultados no se por que
            title = i.xpath("./span[@class='txt']/span[@class='pl']/a/span[@id='titletextonly']/text()").extract()
            title2 = i.xpath("./span[@class='txt']/span[@class='pl']/a/text()").extract()
            print link, title,title2
