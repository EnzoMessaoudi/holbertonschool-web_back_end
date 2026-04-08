#!/usr/bin/env python3

"""
Module that contains a coroutine that take a random number
and print it in certain seconds
"""
import random
from typing import Union
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Take a int as a paramater and return how many time
    passed since the execution
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
