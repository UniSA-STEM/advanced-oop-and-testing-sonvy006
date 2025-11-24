"""
File: staff.py
Description: A brief description of this Python module.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod

class Staff(ABC):

    def __init__(self, staff_id, name, role):
        self.__staff_id = staff_id
        self.__name = name
        self.__role = role
        self.__assigned_animals = []
        self.__assigned_enclosures = []





