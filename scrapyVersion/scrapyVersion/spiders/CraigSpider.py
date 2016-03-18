# -*- coding: utf-8 -*-
import scrapy
import pprint
import re

from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapyVersion.items import Job

class CraigspiderSpider(CrawlSpider):
    name = "CraigSpider"
    allowed_domains = ["losangeles.craigslist.org"] + ["lasvegas.craigslist.org"]
    start_urls = ["http://losangeles.craigslist.org/search/cpg?query=web&is_paid=all"] + ["http://losangeles.craigslist.org/search/cpg"] + ["http://lasvegas.craigslist.org/search/cpg"]

    #start_urls = ["http://losangeles.craigslist.org/search/cpg"]
    #start_urls = ["http://losangeles.craigslist.org/search/cpg?query=web&is_paid=all&srchType=T"]


    #rules = (Rule(LinkExtractor(allow=(r'.*?/.+?/cpg/\d+\.html')), callback='parse_page', follow=False),)
    rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_page", follow= True),)


    def parse_start_url(self, response):
        return self.parse_page(response)


    def parse_page(self, response):
        items = response.selector.xpath("//p[@class='row']")
        #print(len(items))
        items2 = []
        for i in items:


            link = i.xpath("./span[@class='txt']/span[@class='pl']/a/@href").extract()

            #la clase cambia en los siguientes resultados no se por que
            title = i.xpath("./span[@class='txt']/span[@class='pl']/a/span[@id='titletextonly']/text()").extract()
            title2 = i.xpath("./span[@class='txt']/span[@class='pl']/a/text()").extract()

            if not title2:
                #print "http://losangeles.craigslist.org"+link[0].encode("utf-8"), title[0].encode("utf-8")
                #print response.request.url
                #print re.split('/search/(.)',response.request.url)
                url = re.split('/search/(.)',response.request.url) #http://cragislist.sf.org por ejemplo
                #print url[0]+link[0].encode("utf-8") ## link ya parseado
                #print title[0].encode("utf-8") #Titulo ya bien
                item = Job()
                item['title'] = title[0].encode("utf-8")
                item['link'] = url[0]+link[0].encode("utf-8")
                items2.append(item)

            else:
                url = re.split('/search/(.)',response.request.url)
                #print url[0]+link[0].encode("utf-8")
                #print title2[0].encode("utf-8")
                item = Job()
                item['title'] = title2[0].encode("utf-8")
                item['link'] = url[0]+link[0].encode("utf-8")
                items2.append(item)

            yield dict(link=item['link'],title=item['title'])





            #print type(link) te da el tipo de dato muy util!!!
