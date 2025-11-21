"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, animal_id, age, species, dietary_needs):
        self.name = name
        self.animal_id = animal_id
        self.age = age
        self.species = species
        self.dietary_needs = dietary_needs
