#!/usr/bin/env python3
''' asyncio '''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''asynchronous coroutine that takes in an integer argument
    that waits for a random delay between 0 and max_delay
    (included and float value)'''
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
