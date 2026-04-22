#!/usr/bin/env python3

"""
Modulo that contains the function update_topics
    Which takes three paramaters
"""


def update_topics(mongo_collection, name, topics):
    """
        Function that change the topics of mongo_collection
        based on the name
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
