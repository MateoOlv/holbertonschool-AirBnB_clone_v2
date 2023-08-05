#!/usr/bin/python3
""" Place Module for HBNB project """
#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                          Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ Place class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        if getenv("HBNB_TYPE_STORAGE") == "db":
            reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
            amenities = relationship("Amenity", secondary=place_amenity, back_populates="place_amenities", viewonly=False)
