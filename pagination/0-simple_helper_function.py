#!/usr/bin/env python3

def index_range(page, page_size):
    start_page = (page - 1) * page_size
    end = start_page + page_size
    test = (start_page, end)
    return test
