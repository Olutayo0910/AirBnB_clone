#!/usr/bin/python3
""" This module defines all attributes and methods of the User class """
import models
from models.base_model import BaseModel


class User(BaseModel):
    """ Implementation for User class """
    bkeys = ["id", "created_at", "updated_at"]

    def __init__(self, *args, **kwargs):
        """ Initializing new User class """
        super().__init__(**{key: kwargs.get(key) for key in User.bkeys
                            if kwargs.get(key) is not None})
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key not in User.bkeys:
                    self.__dict__[key] = value
