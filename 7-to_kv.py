#!/usr/bin/env python3
"""
Module for task 7: Create a tuple with a string and the square of an int/float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of an int/float.

    Parameters:
    k (str): The string.
    v (Union[int, float]): The int or float to square.

    Returns:
    Tuple[str, float]: A tuple with k and the square of v.
    """
    return (k, float(v ** 2))

