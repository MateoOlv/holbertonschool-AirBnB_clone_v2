#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

print("Init:")
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
    print(storage)
else:
    storage = FileStorage()
    print(storage) # para debuggear
storage.reload()