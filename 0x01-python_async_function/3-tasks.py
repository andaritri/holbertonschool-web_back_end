#!/usr/bin/env python3
"""3-tasks.py file"""


from asyncio import Task, create_task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """task_wait_random function"""
    return create_task(wait_random(max_delay))
