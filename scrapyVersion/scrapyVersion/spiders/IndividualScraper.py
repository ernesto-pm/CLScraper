# -*- coding: utf-8 -*-
import scrapy
import pprint
import re
import urlparse

from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapyVersion.items import Job

class IndividualScraper(scrapy.Spider):
    name = "craig"
    allowed_domains = []
    f = open("links.txt")
    #start_urls = ["https://losangeles.craigslist.org/sfv/cpg/5489867957.html"]
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    download_delay = 3

    def parse(self, response):
        items = response.selector.xpath("//section[@class='body']")
        header = response.selector.xpath("//header[@class='global-header']")
        #print items
        global email2
        for i in items:
            title = i.xpath("//span[@class='postingtitletext']/span[@id='titletextonly']/text()").extract()
            content = i.xpath("//section[@id='postingbody']/text()").extract()
            email = i.xpath("//span[@class='replylink']/a/@href").extract()
            date = i.xpath("//p[@id='display-date']/time[@class='timeago']/text()").extract()

        for h in header:
            location = i.xpath("//li[@class='crumb area']/a/text()").extract()
            #print location



        item = Job()
        item['title'] = ''.join(title)
        item['link'] = response.url
        item['description'] = ''.join(content)
        item['email'] = urlparse.urljoin(response.url, email[0].strip())
        item['date'] = ''.join(date)
        item['location'] = ''.join(location)

        request = scrapy.Request(urlparse.urljoin(response.url, email[0].strip()),callback=self.parse_page2)
        request.meta['item'] = item
        request.meta['proxy'] = "52.91.188.146:8083"
        return request

    def parse_page2(self,response):
        item = response.meta['item']
        items = response.selector.xpath("//div[@class='reply_options']")
        for i in items:
            email2 = i.xpath("//div[@id='webmailinks']/ul/li/div[@class='anonemail']/text()").extract()

        item['email'] = ''.join(email2)
        #print item
        #print type(item)
        #print email
        yield dict(date=item['date'],title=item['title'],link=item['link'],description=item['description'],email=item['email'],location=item['location'])
