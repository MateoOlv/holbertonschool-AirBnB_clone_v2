#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        """relationship with tha class City"""
        cities = relationship("City", cascade='all, delete, delete-orphan',
                            backref='state')
    else:
        name = ""

        @property
        def cities(self):
            from models.city import City
            from models import storage

            results = []
            for element in storage.all(City).values():
                if self.id == element.state_id:
                    results.append(storage.all(City)[element])
            return results