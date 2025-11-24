"""
File: filename.py
Description: Enclosure class for housing animals in the zoo.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Enclosure:
    def __init__(self, enclosure_id, size, environment_type, cleanliness):
        self.__enclosure_id = enclosure_id
        self.__size = size
        self.__environment_type = environment_type
        self.__cleanliness = cleanliness
        self.__animals = []
        self.__animal_type = None

    def get_enclosure_id(self):
        return self.__enclosure_id

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_environment_type(self):
        return self.__environment_type

    def set_environment_type(self, environment_type):
        self.__environment_type = environment_type

    def get_cleanliness(self):
        return self.__cleanliness

    def set_cleanliness(self, cleanliness):
        if cleanliness < 0 or cleanliness > 10:
            raise ValueError("Cleanliness must be between 0 and 10.")
        self.__cleanliness = cleanliness

    def get_animals(self):
        return self.__animals

    def get_animal_type(self):
        return self.__animal_type
