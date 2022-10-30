#!/usr/bin/python3
"""start of command interpreter"""
import re
import cmd
from shlex import split

import models
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
from models.user import User

# A global constant
ClASSES = [
        "BaseModel",
        "City",
        "Amenity",
        "State",
        "Review",
        "Place",
        "User",
        ]

def parse(argmnt):
    c_braces = re.search(r"\{(.*?)\}", argmnt)
    brackets = re.search(r"\[(.*?)\]", argmnt)
    if c_braces is None:
        if berackets is None:
            return [i.strip(",") for i in split(argmnt)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:c_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(c_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True





if __name__ == '__main__':
    HBNBCommand().cmdloop()
