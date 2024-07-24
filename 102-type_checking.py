#!/usr/bin/env python3
"""
Module for task 12: Validate and correct the type annotations.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Create a list by repeating each element in the tuple a given number of times.

    Parameters:
    lst (Tuple[int, ...]): The input tuple.
    factor (int): The repeat factor. Defaults to 2.

    Returns:
    List[int]: The zoomed list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

