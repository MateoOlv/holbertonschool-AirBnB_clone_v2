#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    metadata = Base.metadata
    place_amenity = Table("place_amenity", metadata,
                          Column("place_id", String(60), ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60), ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Amenity(BaseModel, Base):
    """ Amenity class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity, back_populates="amenities")

    else:
        name = ""