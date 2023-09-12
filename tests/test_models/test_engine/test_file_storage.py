#!/usr/bin/python3
"""
file storage tests
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import unittest
import json
import os


class TestFileStorage(unittest.TestCase):
    """
    testing file storage
    """

    def setUp(self):
        """allocating resources"""
        models.storage._FileStorage__objects = {}

    def test_attr(self):
        """testing initialization"""
        self.assertEqual(type(models.storage), FileStorage)
        self.assertEqual(type(models.storage._FileStorage__file_path), str)
        self.assertEqual(type(models.storage._FileStorage__objects), dict)
        self.assertEqual(models.storage._FileStorage__objects, {})

    def test_all(self):
        """testing all"""
        all_objs = models.storage.all()
        self.assertEqual(type(all_objs), dict)
        self.assertEqual(len(all_objs), 0)

    def test_new(self):
        """testing new"""
        obj = BaseModel()
        models.storage.new(obj)
        all_objs = models.storage.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertEqual(all_objs[key], obj)

    def test_save(self):
        """ testing save"""
        obj1 = BaseModel()
        models.storage.save()
        expected = {f"{obj1.__class__.__name__}.{obj1.id}": obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj2 = BaseModel()
        models.storage.save()
        expected = {f"{obj1.__class__.__name__}.{obj1.id}": obj1.to_dict(),
                    f"{obj2.__class__.__name__}.{obj2.id}": obj2.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj3 = BaseModel()
        models.storage.save()
        expected = {f"{obj1.__class__.__name__}.{obj1.id}": obj1.to_dict(),
                    f"{obj2.__class__.__name__}.{obj2.id}": obj2.to_dict(),
                    f"{obj3.__class__.__name__}.{obj3.id}": obj3.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        self.assertEqual(len(models.storage._FileStorage__objects), 3)

    def test_reload(self):
        """testing reload"""
        obj = BaseModel()
        obj = models.storage.all()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        for key, value in obj.items():
            value.to_dict()
            value_dict.append(value.to_dict())
        value1_dict = []
        for key, value in obj1.items():
            value.to_dict()
            value1_dict.append(value.to_dict())
        self.assertEqual(value_dict, value1_dict)

    def tearDown(self):
        """deallocating resources"""
        models.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
