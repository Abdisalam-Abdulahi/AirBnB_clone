#!/usr/bin/python3
"""
city module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class that inherit from BaseModel
    """
    state_id = ""
    name = ""
