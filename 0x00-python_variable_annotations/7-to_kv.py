#!/usr/bin/env python3
"""
Module to convert a string and int/float to a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Parameters:
        k (str): The input string.
        v (Union[int, float]): The input value (integer or float).

    Returns:
        Tuple[str, float]: A tuple contain the string k and
        the square of the int/float v (as a float).
    """
    return (k, v * v)
