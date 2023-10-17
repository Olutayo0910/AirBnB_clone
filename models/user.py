#!/usr/bin/python3
""" This module defines all attributes and methods of the User class """
from models.base_model import BaseModel


class User(BaseModel):
    """User class for representing user objects in the application.

    Public class attributes:
    - email (str): The user's email address.
    - password (str): The user's password.
    - first_name (str): The user's first name.
    - last_name (str): The user's last name.
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new User instance.

        Args:
            *args: Additional arguments (unused).
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
