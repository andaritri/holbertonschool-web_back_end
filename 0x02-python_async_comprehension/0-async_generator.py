#!/usr/bin/env python3
""" 0. async_generator file (task 0)"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator function"""
    for _ in range(10):
        yield random.random()
        await asyncio.sleep(1)
