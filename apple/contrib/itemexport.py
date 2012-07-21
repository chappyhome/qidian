from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter


class CSVOptionRespectingItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter
        super(CSVOptionRespectingItemExporter, self).__init__(*args, **kwargs)
