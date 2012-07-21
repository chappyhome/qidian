# -*- coding: utf-8 -*-

import re
#from scrapy.contrib_exp.crawlspider import Rule
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.contrib.loader.processor import TakeFirst, RemoveTag
from scrapy.contrib.loader.processor import TakeFirst

from apple.contrib.spider import BaseCrawlSpider
from apple.items import NovelItem
from apple.contrib.loader import DefaultXPathItemLoader
from scrapy.selector import HtmlXPathSelector

class QidianSpider(BaseCrawlSpider):
    name = 'qidian'
    allowed_domains = ["qidian.com"]
    regex_home = r'http://all.qidian.com/$'
    regex_list = r'bookstore.aspx\?.*ChannelId=-1&.*PageIndex=\d+'
    regex_item = r'Book/\d+\.aspx$'
    start_urls = [
            'http://all.qidian.com/',
            ]

    rules = [
            Rule(SgmlLinkExtractor(allow=[regex_home]),follow=False, callback='parse_home'),
            Rule(SgmlLinkExtractor(allow=[regex_list]),follow=False, callback='parse_list'),
            Rule(SgmlLinkExtractor(allow=[regex_item]),follow=True,  callback='parse_item'),
            ]
    def parse_home(self, response): # {{{
        #links = self.extract_links(response, allow=self.regex_list)

        m = re.search(ur'GoPage.*1/(\d+).*?页', response.body_as_unicode(), re.M)
        #total_page = int(m.group(1))
	total_page = 1

        reqs = []
        for p in range(1, total_page+1):
            #url = re.sub('PageIndex=\d+', 'PageIndex=%d' % p, links[0].url) 
            url = re.sub('PageIndex=\d+', 'PageIndex=%d' % p, response.url)
            req = self.make_request(url, priority=self.priority_list)
            reqs.append(req)
	print 'ddddddddddddddddddddddddddddddddddddddddddddd'
        return reqs
    # end def }}}

    def parse_list(self, response): # {{{
        reqs = self.extract_requests(response, priority=self.priority_item, allow=self.regex_item)
	print 'ffffffffffffffffffffffffffffffffffffffffffff'
        return reqs
    # end def }}}

    def parse_item(self, response): # {{{
        #loader = DefaultXPathItemLoader(NovelItem(), response=response)
        #loader.add_xpath('name', '//div[@class="title"]/h1')
        #loader.add_xpath('intro', 'div.book_info div.intro div.txt', TakeFirst(), RemoveTag('div'))
        #loader.add_xpath('intro', '//div[@class="txt"]/b', TakeFirst())
        #loader.add_xpath('img_url', '//div[@class="pic_box"]/a/img/@src')
        #loader.add_value('page_url', response.url)
	#print 'aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'

        #item = loader.load_item()
	x = HtmlXPathSelector(response)
	l = NovelItem()
	m = re.search(r'Book/(\d+)\.aspx$',response.url)
	ID = m.group(1)
	l['id'] = ID
	l['name'] = x.select('//div[@class="title"]/h1/text()').extract()[0].replace('\r\n','')	
	intro = x.select('//div[@class="txt"]/b').extract()[0]	
	#re_html = re.compile(r'</?\w+[^>]*>')
	l['intro'] = re.sub(r'</?\w+[^>]*>','',intro).replace('\r\n','')
	#l['intro'] = intro
	l['img_url'] = x.select('//div[@class="pic_box"]/a/img/@src').extract()[0]	
	l['page_url'] = response.url

        return l
        #print item
    # end def }}}

SPIDER = QidianSpider()

