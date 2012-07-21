# -*- coding: utf-8 -*-

#from scrapy.contrib.loader import XPathItemLoader, RegexItemLoader
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Compose
from scrapy.utils.markup import remove_entities

html_processor = Compose(TakeFirst())
text_processor = Compose(TakeFirst(), remove_entities)
class DefaultXPathItemLoader(XPathItemLoader):
    default_output_processor = text_processor
    intro_out = html_processor

