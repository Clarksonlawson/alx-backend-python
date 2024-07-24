#!/usr/bin/env python3
"""
Module for task 11: Safely get a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely get a value from a dictionary.

    Parameters:
    dct (Mapping[Any, T]): The dictionary.
    key (Any): The key to look for.
    default (Union[T, None]): The default value if the key is not found.

    Returns:
    Union[T, None]: The value or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

