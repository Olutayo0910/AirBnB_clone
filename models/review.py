#!/usr/bin/python3
""" This module defines all attributes and methods of the Review class """
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ Implementation for Review class """
    rkeys = ["place_id", "user_id", "text"]

    def __init__(self, *args, **kwargs):
        """ Initializing new Review class """
        super().__init__(**{key: kwargs.get(key) for key in kwargs.keys()
                            if key not in Review.rkeys
                            and kwargs.get(key) is not None})
        self.place_id = ""
        self.user_id = ""
        self.text = ""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in Review.rkeys:
                    self.__dict__[key] = value
