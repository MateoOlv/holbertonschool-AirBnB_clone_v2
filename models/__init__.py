#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
<<<<<<< HEAD


storage = FileStorage()
=======
from models.engine.db_storage import DBStorage
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
>>>>>>> d5311cc94e86f9e72184cc1697d48024b4df0af5
storage.reload()