#!/usr/bin/env python3
""" 0. async_generator """
import time
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator function"""
    for _ in range(10):
        yield random.random()
        await time.sleep(1)
