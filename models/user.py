#!/usr/bin/python3
""" This module defines all attributes and methods of the User class """
import models
from models.base_model import BaseModel


class User(BaseModel):
    """ Implementation for User class """
    def __init__(self, *args, **kwargs):
        """ Initializing new User class """
        super().__init__(**kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "email" or key == "password" or key == \
                        "first_name" or key == "last_name":
                    self.__dict__[key] = value
