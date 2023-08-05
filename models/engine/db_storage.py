#!/usr/bin/python3
"""
this module define a class to manage Db storage
"""
from models.base_model import Base
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """
    this class manages storage of hbnb models
    Private class attributes:
    """
    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        """
        method contructor
        Public instance methods:
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                      (user, password, host, database),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            """delete all table in database"""
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls:
            key = '{}.{}'.format(cls.__name__, cls.id)
            obj_dict = {key: cls for cls in self.__session.query(cls).all()}
        else:
            obj_dict = {}
            for cls in Base.__subclasses__():
                key = '{}.{}'.format(cls.__name__, cls.id)
                obj_dict.update({key: cls for cls in self.__session.query(cls).all()})

        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            del self.__objects[key]

    def reload(self):
        """Create all tables in the database and create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_needed = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(session_needed)
        self.__session = Session
    
    def close(self):
        self.__session.close()
