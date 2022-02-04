#!/usr/bin/env python3
"""
Base Caching System
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache system
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = list(self.cache_data)[0]
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
