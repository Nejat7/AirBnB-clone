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
