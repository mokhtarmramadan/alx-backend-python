#!/usr/bin/env python3
''' asyncio Task '''
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    takes in 2 int arguments (in this order): n and max_delay.
    will spawn wait_random n times with the specified max_delay.
    '''
    random_nums = []
    for _ in range(n):
        random_nums.append(await task_wait_random(max_delay))
    return sorted(random_nums)         
