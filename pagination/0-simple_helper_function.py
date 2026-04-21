#!/usr/bin/env python3

"""
Modulo that contains a function named index_range
which return a tuple that is the begining and the end of a page
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Take two int as parameter and return a tuple
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
