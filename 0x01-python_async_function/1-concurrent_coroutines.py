#!/usr/bin/env python3
''' asyncio '''
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    takes in 2 int arguments (in this order): n and max_delay.
    will spawn wait_random n times with the specified max_delay.
    '''
    random_nums = (await asyncio.gather(*(wait_random(max_delay)
                                        for _ in range(n))))
    return sorted(random_nums)
