#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances"""
            from models.city import City
            from models import storage
            cities_list = []
            for element in storage.all(City).values():
                if self.id == element.state_id:
                    cities_list.append(storage.all(City)[element])
            return cities_list
