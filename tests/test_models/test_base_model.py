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

    def test_init(self):
        """ Testing the initialization process """
        # initializing with __class__ argument
        tb_model = BaseModel(__class__="MyOwn", my_name="TestBase")
        tb_dict = tb_model.to_dict()
        self.assertNotEqual(tb_dict["__class__"], "MyOwn")
        self.assertEqual(tb_dict["my_name"], "TestBase")
        self.assertEqual(tb_dict["__class__"], tb_model.__class__.__name__)

        # initializing with None argument
        tb_model = BaseModel(None)
        tb_dict = tb_model.to_dict()
        tb_keys = tb_dict.keys()
        self.assertEqual(len(tb_dict), 4)
        self.assertIn("__class__", tb_keys)
        self.assertIn("id", tb_keys)
        self.assertIn("created_at", tb_keys)
        self.assertIn("updated_at", tb_keys)
        self.assertNotIn("my_name", tb_keys)

        # initializing with positional arguments
        tb_model = BaseModel(34, "try", "second", True, [])
        tb_dict = tb_model.to_dict()
        self.assertEqual(len(tb_dict), 4)

        tb_model = BaseModel(True, [])
        tb_dict = tb_model.to_dict()
        self.assertEqual(len(tb_dict), 4)

        # initializing with positional and keyword arguments
        my_kw = {"my_name": "SBase", "color": "Green", "my_number": 45}
        tb_model = BaseModel(5, ["list"], False, **my_kw)
        tb_dict = tb_model.to_dict()
        self.assertEqual(len(tb_dict), 4 + len(my_kw))

        # initializing with wrong date format
        self.assertRaises(ValueError, BaseModel, created_at="458648768")
        self.assertRaises(ValueError, BaseModel, updated_at="786987890")

    def test_id(self):
        """ Testing for id uniqueness and authenticity """
        tb_model = BaseModel()
        self.assertIsInstance(tb_model.id, str)
        uid = uuid.UUID(tb_model.id)
        self.assertEqual(uid.version, 4)

        # Testing for uniqueness
        id_list = []
        for i in range(100):
            id_list.append(BaseModel().id)
        id_set = set(id_list)
        self.assertEqual(len(id_list), len(id_set))

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
