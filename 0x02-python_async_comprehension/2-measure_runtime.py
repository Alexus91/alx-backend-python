#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime for four parallel comprehensions
    """
    begin = time.perf_counter()
    outcome = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter() - begin
    return end
