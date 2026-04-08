#!/usr/bin/env python3


"""
Module that contains a function that returns the sum as a float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that take a list of floats and return the sum of all in floats
    """
    res = 0
    for i in input_list:
        res += i
    return res
