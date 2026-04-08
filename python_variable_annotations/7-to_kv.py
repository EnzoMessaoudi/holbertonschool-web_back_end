#!/usr/bin/env python3

"""
Module that contains a function that return a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Take two variable, k(string) and v(int or float) and return a tuple
    wich contains first k and in second the square of v
    """
    return (k, v*v)
