#!/usr/bin/python3
"""
Contains class TestConsole.
"""
import unittest
import cmd
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class TestHBNBCommand(unittest.TestCase):
    """
    Contains tests for console.
    """
    def test_do_create(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "User"
            obj.onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                cls_id = value.id
            output = f.getvalue().strip()
            self.assertEqual(cls_id, output)


if __name__ == '__main__':
    unittest.main()
