#!/usr/bin/env python3
""" 1-async_comprehension.py """
from typing import Generator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[List[float], None, None]:
    """async comprehension function"""
    return [i async for i in async_generator()]
