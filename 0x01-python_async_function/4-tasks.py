#!/usr/bin/env python3
"""4. task final task"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task_wait_n function """
    r = []
    lst = [task_wait_random(max_delay) for _ in range(n)]

    for c in asyncio.as_completed(lst):
        result = await c
        r.append(result)
    return r
