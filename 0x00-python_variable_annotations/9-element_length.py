#!/usr/bin/env python3
"""Annotate the below function’s parameters and return
values with the appropriate types """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to calculate the length of elements in a list.
    """

    return [(i, len(i)) for i in lst]
