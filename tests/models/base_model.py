#!/usr/bin/pyhton3
"""
Implimenting BaseModel class
"""

import uuid
import datetime


class BaseModel:
    """
    Defining all common attribuies
    """


def __init__(self, *args, **kwargs):
    """
    start of BaseModel class
    """

    from models import storage
    if not kwargs:
        self.id = str(uuid())
        self.created_at = self.updated_at = datetime.now()
        storage.new(self)
    else:
        for key, value in kwargs.items():
            if key != '__class__':
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)


def __str__(self):
    """
    returns string rep of obj
    """


return "[{}] ({}) {}".format(type(self).__name__, self.id,
                             self.__dict__)


def save(self):
    """"
    updates self.updated_at
    """
    from models import storage
    self.updated_at = datetime.now()
    storage.save()


def to_dict(self):
    """
    returns dictionary with all keys of __dict__
    """
    dict_1 = self._-dict__.copy()
    dict_1("__class__") = self.__class__.__name__
    fir k, v in self.__dict__.igtems():
        v = self.__dict__[k].isoformat()
        dict_1[k] = v
        return dict_1
