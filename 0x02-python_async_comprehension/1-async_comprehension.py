#!/usr/bin/env python3
"""  Asynchronous Comprehension """
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ 10 random numbers with async comprehensing,
    and return the 10 random numbers.
    """
    outcome = [i async for i in async_generator()]
    return outcome
