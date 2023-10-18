#!/usr/bin/python3
"""doc"""

import uuid
from datetime import date


class BaseModel:
    """doc"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = date.today()
        self.updated_at = date.today()

    def __str__(self) -> str:
        """str"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """doc"""
        self.updated_at = date.today()

    def to_dict(self):
        """dict"""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
