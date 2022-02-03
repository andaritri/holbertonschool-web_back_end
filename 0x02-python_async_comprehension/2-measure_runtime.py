#!/usr/bin/env python3
""" 2-measure_runtime.py """
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_time() -> float:
    """measure_runtime function"""
    start = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time()
    return end - start
