#!/usr/bin/env python3
""" The basics of async  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous that waits for a random delay between 0 and max_delay seconds.

    :param max_delay: The maximum delay for rm_float (default is 10 seconds).
    :return: The random delay.
    """
    rm_float = random.uniform(0, max_delay)
    await asyncio.sleep(ram_float)
    return rm_float
