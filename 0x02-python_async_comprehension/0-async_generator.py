#!/usr/bin/env python3
""" Async Generator """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator, with no arguments looping
    10 times, each time asynchronously wait 1 second, and yield a random number
    between 0 and 10. random module is used.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
