#!/usr/bin/python3
"""
Creates a new database engine
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """
    Creates Database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiates the database
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_MYSQL_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.engine)

    def all(self, cls=None):
        """
        Query on current database session depending on the class name
        """
        dictionary = {}
        for name in classes:
            if cls is None or cls is classes[name] or cls is name:
                objs = self.__session.query(classes[name]).all()
                for obj in objs:
                    key = obj.__class__.name + '.' + obj.id
                    dictionary[key] = obj
        return dictionary
	
    def new(self, obj):
        """
        Adds the object to current db session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from the current db session obj
        """
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session

    def close(self):
        """
        call remove method
        """
        self.__session.remove()