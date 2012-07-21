from scrapy.conf import settings
from scrapy.contrib.exporter import XmlItemExporter


class MyXmlItemExporter(XmlItemExporter):
	def __init__(self, file, **kwargs):
		super(MyXmlItemExporter, self).__init__(file, **kwargs)
		self.item_element = kwargs.pop('item_element', 'doc')
        	self.root_element = kwargs.pop('root_element', 'add')
	def export_item(self, item):
        	self.xg.startElement(self.item_element, {})
        	for name, value in self._get_serialized_fields(item, default_value=''):
            		self._my_export_xml_field(name, value)
        	self.xg.endElement(self.item_element)

	def _my_export_xml_field(self, name, serialized_value):
        	self.xg.startElement("field", {"name":name})
        	if hasattr(serialized_value, '__iter__'):
            		for value in serialized_value:
                		self._export_xml_field('value', value)
        	else:
            		self.xg.characters(serialized_value)
        	self.xg.endElement("field")
