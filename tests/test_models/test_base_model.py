#!/usr/bin/python3
"""
test_base
"""

import unittest
import json
from models.base_model import BaseModel
from datetime import datetime
import uuid
import re
import os


class test_base(unittest.TestCase):
    """class for testing the base"""

	def test_inst(self):
		"""testing instances"""
		my_model = BaseModel()
		self.assertEqual(type(my_model), BaseModel)
		d = datetime.datetime.now().replace(microsecond=0)
		self.assertEqual(my_model.created_at.replace(microsecond=0), d)
		self.assertEqual(my_model.updated_at.replace(microsecond=0), d)
		my_model.name = "My First Model"
		my_model.my_number = 89
		self.assertEqual(my_model.name, "My First Model")
		self.assertEqual(my_model.my_number, 89)
		self.assertEqual(type(my_model.id), type(uuid))
	
	def test_str(self):
		"""should print: [<class name>] (<self.id>) <self.__dict__>"""
		my_model = BaseModel()
		rep = str(my_model)
		class_name = re.search("\[.*\]", rep)
		self_id = re.search("\(.*\)", rep)
		self_dict = re.search("\{.*\}", rep)
		self.assertEqual(class_name, "[BaseModel]")
		self.assertTrue(len(self_id) == 38)
		from_js_dict = json.loads(self_dict)
		inst_dict = my_model.__dict__
		inst_dict["__class__"] = "BaseModel"
		self.assertDictEqual(inst_dict, from_js_dict)
	
	def test_save(self):
		"""check if updated at changes"""
		my_model = BaseModel()
		updated = my_model.updated_at
		my_model.save()
		self.assertNotEqual(updated, my_model.updated_at)
	
	def test_save_not(self):
		"""check if updated doesn't change"""
		my_model = BaseModel()
		updated = my_model.updated_at
		str(my_model)
		self.assertEqual(updated, my_model.updated_at)
	
	def test_to_dict(self):
		"""check dict"""
		my_model = BaseModel()
		my_model_json = my_model.__dict__
		my_model_json["__class__ "] = "BaseModel"
		my_model_json["created_at"] = my_model_json["created_at"].isoformat()
		my_model_json["updated_at"] = my_model_json["updated_at"].isoformat()
		from_js_dict = json.loads(my_model.to_dict())
		self.assertDictEqual(my_model_json, from_js_dict)

if __name__ == '__main__':
    unittest.main()

		


		
