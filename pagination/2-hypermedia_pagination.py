#!/usr/bin/env python3

"""
Modulo that contains one class and two functions
    Server: Import the database
        dataset: Return a list with the datas
        get_page: Return the data with the good index
        get_hyper: Return a dictionnray with the data, next,
            previous and total of element in a page
"""


import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Take page and page_list as parameter
            return a list with the information at the good index
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        index = index_range(page, page_size)

        return self.dataset()[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Function that take two int as a parameter and return a dictionnary
        """
        data = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        if page == total_pages:
            next_page = None
        else:
            next_page = page + 1

        res = {"page_size": page_size, "page": page, "data": data,
               "next_page": next_page, "prev_page": prev_page,
               "total_pages": total_pages}

        return res
