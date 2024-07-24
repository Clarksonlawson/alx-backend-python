#!/usr/bin/env python3
"""
Module for task 10: Return the first element of a sequence or None.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence or None if the sequence is empty.

    Parameters:
    lst (Sequence[Any]): The sequence.

    Returns:
    Union[Any, None]: The first element or None.
    """
    if lst:
        return lst[0]
    else:
        return None

