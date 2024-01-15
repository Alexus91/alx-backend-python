#!/usr/bin/env python3
"""  1. Let's execute multiple coroutines at the same time with async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Let's execute multiple coroutines at the same time with async  """
    delay_coroutines: List[float] = []
    all_delays: List[float] = []

    for _ in range(n):
        delay_coroutines.append(wait_random(max_delay))

    for delay_task in asyncio.as_completed(delay_coroutines):
        earliest_result = await delay_task
        all_delays.append(earliest_result)

    return all_delays
