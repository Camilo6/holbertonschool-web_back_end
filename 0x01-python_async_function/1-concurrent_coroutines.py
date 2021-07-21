#!/usr/bin/env python3
"""a asynchronous coroutine"""

import asyncio  
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n : int, max_delay: int) -> float:
    """returns a delayed value"""
    delayed_value = wait_random(n)
    await asyncio.sleep(delayed_value)
    return delayed_value
