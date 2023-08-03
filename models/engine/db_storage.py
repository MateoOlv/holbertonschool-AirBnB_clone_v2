from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.place import Place

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}

class DBStorage:
    """
    Database Storage Class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        DBStorage class instances
        """
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_password = getenv("HBNB_MYSQL_PWD")
        mysql_host = getenv("HBNB_MYSQL_HOST")
        mysql_db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(mysql_user, mysql_password,
                                              mysql_host, mysql_db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Dictionary of all objects
        """
        objects = {}
        if cls:
            if type(cls) == str:
                cls = classes[cls]
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            for cls in classes.values():
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

    def new(self, obj):
        """
        Adds objects to the database in the current session
        """
        self.__session.add(obj)

    def save(self):
        """
        Save object to the database in the current session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete objets from current session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Load objects from database
        Create a new session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        self.__session.close()

