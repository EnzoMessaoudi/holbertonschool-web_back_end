#!/usr/bin/env python3

"""
    Modulo that contains the function schools_by_topic
        which takes two paramaters
"""


def schools_by_topic(mongo_collection, topic):
    """
        Function that return a list of school having a
        specific topic
    """
    return mongo_collection.find({"topic": topic})
