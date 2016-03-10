# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor

class CraigspiderSpider(scrapy.Spider):
    name = "CraigSpider"
    allowed_domains = ["http://losangeles.craigslist.org/search/cpg/"]
    start_urls = (
        'http://losangeles.craigslist.org/search/cpg/',
    )

    def parse(self, response):
        for sel in response.xpath("//span[@class='pl']"):
            link = sel.xpath('a/@href').extract()
            #print link

        for sel in response.xpath("//span[@id='titletextonly']"):
            title = sel.xpath('text()').extract()
            #print title

        items = response.selector.xpath("//p[@class='row']")
        for i in items:
            link = i.xpath("./span[@class='txt']/span[@class='pl']/a/@href").extract()
            title = i.xpath("./span[@class='txt']/span[@class='pl']/a/span[@id='titletextonly']/text()").extract()
            print link,title
