#!/usr/bin/env python3
''' async comprehension '''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measures runtime after executing async_comprehension
    four times in parallel '''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    elapsed = time.perf_counter() - start
    return elapsed
