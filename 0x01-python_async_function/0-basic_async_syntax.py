#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it."""
import asyncio
import random


async def wait_random(max_dealay: int = 10) -> float:
    """0-basic_async_syntax.py"""
    t = random.randint(0, max_dealay)
    await asyncio.sleep(t)
    return t


wait_random = wait_random
