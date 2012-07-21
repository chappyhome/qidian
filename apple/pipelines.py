from apple.contrib.store import StoreItem

class StoragePipeline(StoreItem):
    def process_item(self, item, spider): # {{{
        self.store_item(item, spider)
	#print str(item) + 'aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
        return item
    # end def }}}

