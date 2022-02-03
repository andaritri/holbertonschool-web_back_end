#!/usr/bin/env python3
"""
Base Caching System
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Base Cache system
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
