#!/usr/bin/env python3

"""
    Modulo that contains the function list_all
        Takes one paramater
"""


def list_all(mongo_collection):
    """
    Function which return a list of all documents inside
    of a collection.
    """
    res = mongo_collection.find()

    if not res:
        return []

    return list(res)
