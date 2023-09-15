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
import os
import json


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
    
    def test_do_destroy_Base(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "BaseModel"
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "BaseModel"
            obj.onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_Base2(self):
        """test destroy"""
        id = ""
        cls_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls_name}.destroy({id})"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
        
    
    def test_do_destroy_User(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "User"
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "User"
            obj.onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_User2(self):
        """test destroy"""
        id = ""
        cls_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls_name}.destroy({id})"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_Amen(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "Amenity"
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "Amenity"
            obj.onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_Amen2(self):
        """test destroy"""
        id = ""
        cls_name = "Amenity"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls_name}.destroy({id})"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_City(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "City"
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "City"
            obj.onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_City2(self):
        """test destroy"""
        id = ""
        cls_name = "City"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls_name}.destroy({id})"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Place(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "Place"
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "Place"
            obj.onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_Place2(self):
        """test destroy"""
        id = ""
        cls_name = "Place"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls_name}.destroy({id})"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Review(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "Review"
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "Review"
            obj.onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_Review2(self):
        """test destroy"""
        id = ""
        cls_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls_name}.destroy({id})"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_State(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "State"
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "State"
            obj.onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_State2(self):
        """test destroy"""
        id = ""
        cls_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls_name}.destroy({id})"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)
    
    def test_do_destroy_arg1_miss(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"destroy")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")
    
    def test_do_destroy_arg1_miss2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f".destroy()"))
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")
    
    def test_do_destroy_arg1_incorrect(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"destroy hi")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")
    
    def test_do_destroy_arg1_incorrect2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"hi.destroy()"))
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")
    
    def test_do_destroy_arg2_miss(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")
    
    def test_do_destroy_arg2_miss2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"BaseModel.destroy()"))
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")
    
    def test_do_destroy_arg2_incorrect(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"destroy BaseModel 123")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")
    
    def test_do_destroy_arg2_incorrect2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"BaseModel.destroy(123)"))
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")
    
    def test_do_all(self):
        """test all"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all")
            output = f.getvalue().strip()
            self.assertEqual(output,  "[]")
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            cls_name = "State"
            obj.onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"State.{id}"]) + '"]'
            self.assertEqual(rep,  output)
    
    def test_do_all_Base(self):
        """test all"""
        id = ""
        cls1_name = "BaseModel"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls1_name}.all()"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
    
    def test_do_all_User(self):
        """test all"""
        id = ""
        cls1_name = "User"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls1_name}.all()"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
    
    def test_do_all_Amen(self):
        """test all"""
        id = ""
        cls1_name = "Amenity"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls1_name}.all()"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
    
    def test_do_all_City(self):
        """test all"""
        id = ""
        cls1_name = "City"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls1_name}.all()"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
    
    def test_do_all_Place(self):
        """test all"""
        id = ""
        cls1_name = "Place"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls1_name}.all()"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
    
    def test_do_all_Review(self):
        """test all"""
        id = ""
        cls1_name = "Review"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls1_name}.all()"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
    
    def test_do_all_State(self):
        """test all"""
        id = ""
        cls1_name = "State"
        cls2_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"{cls1_name}.all()"))
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
    
    def test_do_all_Err(self):
        """test all"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"all No")
            output = f.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)
    
    def tearDown(self):
        """deallocating resources"""
        models.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
