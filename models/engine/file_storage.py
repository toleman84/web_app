#!/usr/bin/python3
"""doc"""


class FileStorage:
    """doc"""
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        self.__objects[obj.__class__.__name__+"."+obj.id] = obj
