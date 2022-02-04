#!/usr/bin/env python3
"""
Base Caching System
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """FIFOCache system
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.pop(key)
                else:
                    discard = list(self.cache_data)[0]
                    self.cache_data.pop(discard)
                    print("DISCARD: {}".format(discard))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
