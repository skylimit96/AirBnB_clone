#!/usr/bin/python3
"""Defines the AirBnB BaseModel"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is the BaseModel of our project"""

    def __init__(self, *args, **kwargs):
        """Init the BaseModel :

        Args:
            *args (any): will not be used in this project.
            **kwargs (dict): attributes represented as Key/Val.
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """function to update (updated_at) to current time."""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Returns the string representation of our BaseModel"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
    
    def to_dict(self):
        """Return the dict of our BaseModel.

        Includes the key/Val __class__ representing
        the name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
