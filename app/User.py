""" User Model """

from src.masoniteorm.orm import Model


class User(Model):
    """User Model 
    """

    __fillable__ = ['name', 'email', 'password']

    __connection__ = 'mysql'

    __auth__ = 'email'
