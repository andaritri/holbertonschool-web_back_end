#!/usr/bin/env python3
"""1-concurrent courotines task"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function that call wait_random function"""
    result = []
    lst = [wait_random(max_delay) for _ in range(n)]
    for c in asyncio.as_completed(lst):
        r = await c
        result.append(r)
    return result
