#!/usr/bin/env python3
''' asyncio '''
import asyncio
from time import perf_counter

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time for wait_n(n, max_delay) """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    measure_value = elapsed / n
    return measure_value
