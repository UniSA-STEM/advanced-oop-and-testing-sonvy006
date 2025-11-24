"""
File: animal.py
Description: A brief description of this animal.py file
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, animal_id, age, species, dietary_needs):
        self.__name = name
        self.__animal_id = animal_id
        self.__age = age
        self.__species = species
        self.__dietary_needs = dietary_needs

    def get_animal_id(self):
        return self.__animal_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def get_dietary_needs(self):
        return self.__dietary_needs

    def set_age(self, age):
        if age < 0:
            raise ValueError('Age cannot be negative')
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def sleep(self):
        return f"{self.__name} is peacefully sleeping."

    def __str__(self):
        return f"{self.__name} ({self.__species}), Age: {self.__age}"

    def __eq__(self, other):
        return isinstance(other, Animal) and self.__animal_id == other.__animal_id









