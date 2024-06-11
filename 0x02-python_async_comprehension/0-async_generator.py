#!/usr/bin/env python3
''' async generator '''
import asyncio
import random


async def async_generator():
    ''' loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10 '''
    for _ in range(10):
        await asyncio.sleep(1)
        random_number = random.uniform(0, 10)
        yield random_number
