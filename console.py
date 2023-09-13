#!/usr/bin/python3
"""console"""
from models import storage
from models.base_model import BaseModel
from models.user import User
import models
import cmd
import shlex

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_create(self, line):
        """creates a new instance of BaseModel"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        classes = {"User": User, "BaseModel": BaseModel}
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[cls_name]()
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
        classes = ["User", "BaseModel"]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id = args[1]
        ##getting the list of all objects
        dictionary = storage.all()
        key = f"{cls_name}.{id}"
        if key in dictionary:
            ##dictionary[key] is an object
            print(dictionary[key])
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
        classes = ["User", "BaseModel"]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        ##getting the list of all objects
        id = args[1]
        dictionary = storage.all()
        key = f"{cls_name}.{id}"
        if key in dictionary:
            ##dictionary[key] is the object
            del(dictionary[key])
            ##now delete the key from the dictionary
            storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name"""
        args = line.split()
        if len(args) == 1:
            cls_name = args[0]
            classes = ["User", "BaseModel"]
            if cls_name not in classes:
                print("** class doesn't exist **")
                return
            ##getting the list of all objects
            dictionary = storage.all()
            for key in dictionary:
                ##dictionary[key] is an object
                if dictionary[key].__class__.__name__ == cls_name:
                    print(dictionary[key])
        else:
            dictionary = storage.all()
            for key in dictionary:
                print(dictionary[key])
    
    def do_update(self, line):
        """updates obj
        update <class name> <id> <attribute name> "<attribute value>"""

        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        cls_list = ["User", "BaseModel"]
        if cls_name not in cls_list:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        id = args[1]
        dictionary = storage.all()
        key = f"{cls_name}.{id}"
        if key not in dictionary:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = dictionary[key]
        attr = args[2]
        val = args[3]
        if hasattr(obj, attr):
            value = getattr(obj, attr)
            if type(value) is int or type(value) is float:
                if int(val) == float(val):
                    setattr(obj, attr, int(val))
                else:
                    setattr(obj, attr, float(val))
            else:
                setattr(obj, attr, val)
        else:
            setattr(obj, attr, val)
        obj.save()
        
    
    def do_EOF(self, line):
        """quit the program"""
        return True
    
    def do_quit(self, line):
        """quit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
