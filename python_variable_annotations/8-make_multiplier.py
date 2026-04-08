#!/usr/bin/env python3

"""
Module that contains a function wich return a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    take a float as parameter and return a function that multiply the paramater
    """
    def multiply(x: float) -> float:
        """
        Multiply the paramater passed to it
        """
        return x * multiplier
    return multiply
