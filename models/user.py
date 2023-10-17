#!/usr/bin/python3
""" This module defines all attributes and methods of the User class """
from models.base_model import BaseModel


class User(BaseModel):
    """Implementation for User class"""
    def __init__(self, *args, **kwargs):
        """Initialize a new User."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
