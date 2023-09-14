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
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)
        with patch('sys.stdout', new=StringIO()) as f1:
            obj1 = HBNBCommand()
            obj1.onecmd(f"create")
            output1 = f1.getvalue().strip()
            expected_msg1 = "** class name missing **"
            self.assertEqual(expected_msg1, output1)
        with patch('sys.stdout', new=StringIO()) as f2:
            obj2 = HBNBCommand()
            cls_name = "MyModel"
            obj2.onecmd(f"create {cls_name}")
            output2 = f2.getvalue().strip()
            expected_msg2 = "** class doesn't exist **"
            self.assertEqual(expected_msg2, output2)

    def test_do_count(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "User"
            obj.onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            self.assertEqual(expected_count, int(output))

    def test_do_show(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            dictionary = models.storage.all()
            cls_name = "City"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                obj.onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)
        with patch('sys.stdout', new=StringIO()) as f1:
            obj1 = HBNBCommand()
            obj1.onecmd(f"show")
            output1 = f1.getvalue().strip()
            expected_msg1 = "** class name missing **"
            self.assertEqual(expected_msg1, output1)
        with patch('sys.stdout', new=StringIO()) as f2:
            obj2 = HBNBCommand()
            cls_name = "MyModel"
            obj2.onecmd(f"show {cls_name}")
            dictionary = models.storage.all()
            output2 = f2.getvalue().strip()
            expected_msg2 = "** class doesn't exist **"
            self.assertEqual(expected_msg2, output2)
        with patch('sys.stdout', new=StringIO()) as f3:
            obj3 = HBNBCommand()
            cls_name = "Amenity"
            obj3.onecmd(f"show {cls_name}")
            dictionary = models.storage.all()
            output3 = f3.getvalue().strip()
            expected_msg3 = "** instance id missing **"
            self.assertEqual(expected_msg3, output3)
        with patch('sys.stdout', new=StringIO()) as f4:
            obj4 = HBNBCommand()
            cls_name = "Place"
            obj4.onecmd(f"show {cls_name} My_First_Model")
            output4 = f4.getvalue().strip()
            expected_msg4 = "** no instance found **"
            self.assertEqual(expected_msg4, output4)

    def tearDown(self):
        """deallocating resources"""
        models.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
