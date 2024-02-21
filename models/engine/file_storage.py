#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review}

class FileStorage:
    """ manages storage of hbnb as JSON """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ dictionary in storage returned """
        f_b_c = {}
        if cls:
            for op, vlvl in FileStorage.__objects.items():
                if vlvl.__class__ == cls or vlvl.__class__.__name__ ==cls:
                    f_b_c[op] = vlvl
            return f_b_c
        return FileStorage.__objects

    def new(self, obj):
        """ new object added to dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dict"""
        with open(FileStorage.__file_path, 'w') as fillle:
            sto = {}
            sto.update(FileStorage.__objects)
            for op, vlvl in sto.items():
                sto[op] = vlvl.to_dict()
            json.dump(sto, fillle)

    def reload(self):
        """Loads storage dictionary"""
      
        try:
            sto = {}
            with open(FileStorage.__file_path, 'r') as fillle:
                sto = json.load(fillle)
                for op, vlvl in sto.items():
                    self.all()[op] = classes[vlvl['__class__']](**vlvl)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        ''' delete obj  '''
        if obj:
            op = '{}.{}'.format(type(obj).__name__, obj.id)
            del FileStorage.__objects[op]

    def close(self):
        """ Deserialize JSON file to objects before closing """
        self.reload()
