#!/usr/bin/env python3

"""
Module that contains a function measure_time
Count how many seconds apssed since the execution of the function wait_n
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Take n and max_delay (two int) as parameters
    Return a float
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start

    return total_time / n
