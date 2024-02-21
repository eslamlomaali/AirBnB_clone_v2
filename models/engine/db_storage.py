#!/usr/bin/python3
""" Database Storage handling """
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.amenity import Amenity


class DBStorage:
    '''
     db engine handling
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        engine created for database
        '''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        query for all obj on session
        '''
       classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

        rsrs = {}
        q_r = []

        if cls:
            '''Query for all obj'''
            if type(cls) is str:
                cls = eval(cls)
            q_r = self.__session.query(cls)
            for obj in q_r:
                op = '{}.{}'.format(type(obj).__name__, obj.id)
                rsrs[op] = obj
            return rsrs
        else:
            '''Query for all types'''
            for nmnm, vlvl in classes.items():
                q_r = self.__session.query(vlvl)
                for obj in q_r:
                    op = '{}.{}'.format(nmnm, obj.id)
                    result[op] = obj
            return rsrs

    def new(self, obj):
        '''add obj to the session'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete data from session'''
        if obj is not None:
           self.__session.delete(obj)

    def reload(self):
	''' reload data at the db '''
        Base.metadata.create_all(self.__engine)
        ses_fact = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
       calling method remove() at session
        """
        self.__session.close()
