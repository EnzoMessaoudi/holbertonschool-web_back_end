#!/usr/bin/env python3

"""
Module that include a function that return a sum of floats and integers
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that take a list of int and floats and return the sum in float
    """
    res = 0
    for i in mxd_lst:
        res += i
    return res
