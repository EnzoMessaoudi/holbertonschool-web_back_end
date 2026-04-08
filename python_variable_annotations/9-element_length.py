#!/usr/bin/env python3

"""
Module that contains a function wich take a Sequence as a paramater
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that take a Sequence as a parameter and returns a list
    """
    return [(i, len(i)) for i in lst]
