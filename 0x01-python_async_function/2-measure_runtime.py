#!/usr/bin/env python3
"""
Measure runtime module
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time per coroutine call for wait_n(n, max_delay).
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n

