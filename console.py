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
