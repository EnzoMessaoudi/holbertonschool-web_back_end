#!/usr/bin/env python3

"""
    Modulo that contains the function insert_school
        Takes two arguments
"""


def insert_school(mongo_collection, **kwargs):
    """
        Function that insert a doc inside mongo_collection
        returns the new id
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
