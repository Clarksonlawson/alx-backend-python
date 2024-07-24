#!/usr/bin/env python3
"""
Module for task 8: Return a function that multiplies a float by a given multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a given multiplier.

    Parameters:
    multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: A function that multiplies a float by multiplier.
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func

