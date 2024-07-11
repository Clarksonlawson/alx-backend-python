#!/usr/bin/env python3
"""
Tasks module
"""

import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task object for wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))

