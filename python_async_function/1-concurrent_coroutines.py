#!/usr/bin/env python3

"""
Module that import wait_random (latest task) and return a list
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that take two arguments and return a list of floats
    """
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    delays = []

    for task in tasks:
        delays.append(await task)

    return sorted(delays)
