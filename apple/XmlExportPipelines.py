import time
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
#from scrapy.contrib.exporter import XmlItemExporter
from apple.contrib.XmlItemExporter import MyXmlItemExporter



class XmlExportPipeline(object):

    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
	self.count = 0
	self.open_new_file()

    def spider_opened(self, spider):
        pass

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def open_new_file(self):
	timestampt = time.time()
        self.file = open('/tmp/%s_products.xml' % timestampt, 'w+b')
	self.exporter = MyXmlItemExporter(self.file)
        self.exporter.start_exporting()
		

    def process_item(self, item, spider):
	self.count+=1
	if self.count>10:
		self.exporter.finish_exporting()
		self.file.close()
		self.open_new_file()
		self.count = 0
        self.exporter.export_item(item)
        return item
