#!/usr/bin/env python3
""" Take the code from wait_n and alter it into a new function task_wait_n."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Tasks """
    delays: List[float] = []
    sum_delays: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        sum_delays.append(earliest_result)
    return sum_delays
