# Scrapy settings for apple project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

BOT_NAME = 'apple'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['apple.spiders']
NEWSPIDER_MODULE = 'apple.spiders'
DEFAULT_ITEM_CLASS = 'apple.items.NovelItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

#ITEM_PIPELINES = [
#    'apple.pipelines.StoragePipeline',
#]
#FEED_EXPORTERS = {
#    'csv': 'apple.contrib.itemexport.CSVOptionRespectingItemExporter',
#}
#DB_URL = 'mysql://root:@localhost/spiderdb?charset=utf8&use_unicode=0'
#DB_TABLE = 'novel_items'
#DEPTH_LIMIT = 3

ITEM_PIPELINES = [
    'apple.XmlExportPipelines.XmlExportPipeline',
]
