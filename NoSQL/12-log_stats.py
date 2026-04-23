#!/usr/bin/env python3

"""
    Modulo that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")

    db = client["logs"]
    collection = db["nginx"]

    number = collection.count_documents({})
    print("{} logs".format(number))

    print("Methods:")

    meth_get = collection.count_documents({"method": "GET"})
    print("\tmethod GET: {}".format(meth_get))

    meth_post = collection.count_documents({"method": "POST"})
    print("\tmethod POST: {}".format(meth_post))

    meth_put = collection.count_documents({"method": "PUT"})
    print("\tmethod PUT: {}".format(meth_put))

    meth_patch = collection.count_documents({"method": "PATCH"})
    print("\tmethod PATCH: {}".format(meth_patch))

    meth_delete = collection.count_documents({"method": "DELETE"})
    print("\tmethod DELETE: {}".format(meth_delete))

    num_doc = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(num_doc))
