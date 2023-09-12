#!/usr/bin/python3
"""console"""
from models import storage
from models.base_model import BaseModel
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """quit the program"""
        return True
    
    def do_quit(self, line):
        """quit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()