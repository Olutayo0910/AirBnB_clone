#!/usr/bin/python3
""" This implements tests for the BaseModel class """
import unittest
import uuid
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ BaseModel unittest class """

    @classmethod
    def setUpClass(cls):
	    pass

    def test_id(self):
        """ Testing for id uniqueness and authenticity """
        tb_model = BaseModel()
        self.assertIsInstance(tb_model.id, str)
        uid = uuid.UUID(tb_model.id)
        self.assertEqual(uid.version, 4)

    def test_dates(self):
        """ Testing dates for awareness and consistency """
        tb_model = BaseModel()
        created_at = tb_model.created_at
        updated_at = tb_model.updated_at

        self.assertIsInstance(created_at, datetime.datetime)
        self.assertIsNone(created_at.tzinfo)

        self.assertIsInstance(updated_at, datetime.datetime)
        self.assertIsNone(updated_at.tzinfo)

        tb_model.save()
        updated_at = tb_model.updated_at
        self.assertIs(created_at < updated_at, True)
