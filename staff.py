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

    def get_staff_id(self):
        return self.__staff_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_role(self):
        return self.__role

    def get_assigned_animals(self):
        return self.__assigned_animals

    def assign_animal(self, animal):
        if animal not in self.__assigned_animals:
            self.__assigned_animals.append(animal)

    def unassign_animal(self, animal):
        if animal in self.__assigned_animals:
            self.__assigned_animals.remove(animal)

    def get_assigned_enclosures(self):
        return self.__assigned_enclosures

    def assign_enclosure(self, enclosure):
        if enclosure not in self.__assigned_enclosures:
            self.__assigned_enclosures.append(enclosure)

    def unassign_enclosure(self, enclosure):
        if enclosure in self.__assigned_enclosures:
            self.__assigned_enclosures.remove(enclosure)






