#!/usr/bin/python3
""" This module defines all attributes and methods of the Place class """
import models
from models.base_model import BaseModel


class Place(BaseModel):
    """ Implementation for Place class """
    pkeys = ["city_id", "user_id", "name", "description", "number_rooms",
             "number_bathrooms", "max_guest", "price_by_night", "latitude",
             "longitude", "ammenity_ids"]

    def __init__(self, *args, **kwargs):
        """ Initializing new Place class """
        super().__init__(**{key: kwargs.get(key) for key in kwargs.keys()
                            if key not in Place.pkeys
                            and kwargs.get(key) is not None})
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in Place.pkeys:
                    self.__dict__[key] = value
