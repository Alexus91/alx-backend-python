#!/usr/bin/env python3
"""  1. Let's execute multiple coroutines at the same time with async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random.

    :param n: Number of times to spawn wait_random.
    :param max_delay: The maximum delay for each wait_random call.
    :return: List of delays in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)
