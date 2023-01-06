#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models.__init__


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.__init__.storage_type == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), nullable=False, ForeignKey=('states.id'))
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities')
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
