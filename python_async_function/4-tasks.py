#!/usr/bin/env python3

"""
Module that imports task_wait_random and returns a list
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that takes two arguments and returns a list of floats.
    Creates n asyncio tasks using task_wait_random and collects their results.
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    results = []
    for task in tasks:
        results.append(await task)

    return sorted(results)
