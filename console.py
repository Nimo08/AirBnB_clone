#!/usr/bin/python3
"""console"""
from models import storage
from models.base_model import BaseModel
import models
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_create(self, line):
        """creates a new instance of BaseModel"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in globals():
            print("** class doesn't exist **")
            return
        obj = BaseModel()
        models.storage.save()
        print(obj.id)

    def do_show(self, line):
        """Prints the str rep of an instance based
        on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if f"{__class__.__name__}.{id}" in storage._FileStorage__objects:
            print(obj)
        else:
            print("** no instance found **")
            return

    def do_destroy(self, line):
        """Deletes an instance based on the
        class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if f"{__class__.__name__}.{id}"in storage._FileStorage__objects:
            del(obj)
        else:
            print("** no instance found **")
            return

    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name"""
        args = line.split()
        cls_name = args[0]
        if cls_name not in globals():
            print("** class doesn't exist **")
            return
        ##getting the list of all objects
        dictionary = storage.all()
        for key in dictionary:
            ##dictionary[key] is an object
            if dictionary[key].__class__.__name__ == cls_name:
                print(dictionary[key])
    
    def do_EOF(self, line):
        """quit the program"""
        return True
    
    def do_quit(self, line):
        """quit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
