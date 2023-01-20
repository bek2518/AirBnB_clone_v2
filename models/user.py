#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if models.storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user')
        reviews = relationship('Review', backref='user')

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    @property
    def reviews(self):
        review_list = []
        all_reviews = models.storage.all(Review)
        for city in all_reviews.values():
            if city.state_id == self.id:
                review_list.append(city)
        return review_list