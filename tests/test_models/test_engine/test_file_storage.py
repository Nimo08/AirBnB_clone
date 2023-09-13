#!/usr/bin/python3
"""
file storage tests
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
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

    def test_new_BaseModel(self):
        """testing new"""
        obj = BaseModel()
        models.storage.new(obj)
        all_objs = models.storage.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertEqual(all_objs[key], obj)
    
    def test_new_User(self):
        """testing new"""
        obj = User()
        all_objs = models.storage.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertEqual(all_objs[key], obj)
    
    def test_new_all(self):
        """testing new"""
        obj = User()
        obj2 = BaseModel()
        all_objs = models.storage.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertEqual(all_objs[key], obj)
        key = f"{obj2.__class__.__name__}.{obj2.id}"
        self.assertEqual(all_objs[key], obj2)

    def test_save_BaseModel(self):
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
    
    def test_save_User(self):
        """ testing save"""
        obj1 = User()
        models.storage.save()
        expected = {f"{obj1.__class__.__name__}.{obj1.id}": obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj2 = User()
        models.storage.save()
        expected = {f"{obj1.__class__.__name__}.{obj1.id}": obj1.to_dict(),
                    f"{obj2.__class__.__name__}.{obj2.id}": obj2.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj3 = User()
        models.storage.save()
        expected = {f"{obj1.__class__.__name__}.{obj1.id}": obj1.to_dict(),
                    f"{obj2.__class__.__name__}.{obj2.id}": obj2.to_dict(),
                    f"{obj3.__class__.__name__}.{obj3.id}": obj3.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        self.assertEqual(len(models.storage._FileStorage__objects), 3)
    
    def test_save_all(self):
        """ testing save"""
        obj1 = User()
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

    def test_reload_BaseModel(self):
        """testing reload"""
        BaseModel()
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
    
    def test_reload_User(self):
        """testing reload"""
        User()
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
    
    def test_reload_User(self):
        """testing reload"""
        user = User()
        base = BaseModel()
        key_user = f"{user.__class__.__name__}.{user.id}"
        key_base = f"{base.__class__.__name__}.{base.id}"
        obj = models.storage.all()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        value_dict.append(obj[key_user].to_dict())
        value_dict.append(obj[key_base].to_dict())
        value1_dict = []
        value1_dict.append(obj1[key_user].to_dict())
        value1_dict.append(obj1[key_base].to_dict())
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
