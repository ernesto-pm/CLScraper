# -*- coding: utf-8 -*-
import scrapy
import pprint
import re
import urlparse

from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapyVersion.items import Job
from selenium import webdriver

class IndividualScraper(scrapy.Spider):
    name = "craig"
    allowed_domains = []
    f = open("links.txt")
    #start_urls = ["https://losangeles.craigslist.org/sfv/cpg/5489867957.html"]
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    def parse(self, response):

        items = response.selector.xpath("//section[@class='body']")
        #print items
        for i in items:
            title = i.xpath("//span[@class='postingtitletext']/span[@id='titletextonly']/text()").extract()
            content = i.xpath("//section[@id='postingbody']/text()").extract()
            email = i.xpath("//span[@class='replylink']/a/@href").extract()
            date = i.xpath("//p[@id='display-date']/time[@class='timeago']/text()").extract()

            #print content[0].encode("utf-8")
        item = Job()
        item['title'] = ''.join(title)
        item['link'] = response.url
        item['description'] = ''.join(content)
        item['email'] = urlparse.urljoin(response.url, email[0].strip())
        item['date'] = ''.join(date)

        #yield dict(title=item['title'],link=item['link'],description=item['description'],email=item['email'])
        yield dict(date=item['date'],title=item['title'],link=item['link'],description=item['description'],email=item['email'])

        #print ''.join(title)
        #print ''.join(content)
        #print urlparse.urljoin(response.url, email[0].strip())
        #print response.url





        #items = response.selector.xpath("//p[@class='row']")
        #items2 = []
        #for i in items:
            #link = i.xpath("./span[@class='txt']/span[@class='pl']/a/@href").extract()
            #title = i.xpath("./span[@class='txt']/span[@class='pl']/a/span[@id='titletextonly']/text()").extract()
            #title2 = i.xpath("./span[@class='txt']/span[@class='pl']/a/text()").extract()

            #if not title2:
                #url = re.split('/search/(.)',response.request.url)
                #print url[0]+link[0].encode("utf-8")


            #else:
                #url = re.split('/search/(.)',response.request.url)
                #print url[0]+link[0].encode("utf-8")
