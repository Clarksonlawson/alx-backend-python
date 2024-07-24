#!/usr/bin/env python3
"""
Module for task 6: Sum a mixed list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a mixed list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): The mixed list of integers and floats.

    Returns:
    float: The sum of the elements in mxd_lst.
    """
    return sum(mxd_lst)

