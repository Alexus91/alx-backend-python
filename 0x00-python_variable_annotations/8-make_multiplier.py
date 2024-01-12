#!/usr/bin/env python3
"""
Module to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function to create a multiplier function.

    Returns:
        Callable[[float], float]: A function that takes
        a float and multiplies it by the given multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
