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

    def add_animal(self, animal):
        if self.__animal_type is None:
            self.__animal_type = animal.__class__.__name__
        elif self.__animal_type != animal.__class__.__name__:
            raise ValueError(f"Cannot mix {animal.__class__.__name__} with {self.__animal_type}.")

        if animal in self.__animals:
            raise ValueError(f"{animal.get_name()} is already in this enclosure.")

        self.__animals.append(animal)

    def remove_animal(self, animal):
        if animal not in self.__animals:
            raise ValueError(f"{animal.get_name()} is not in this enclosure.")

        self.__animals.remove(animal)

        if len(self.__animals) == 0:
            self.__animal_type = None

    def get_status(self):
        animal_count = len(self.__animals)
        animal_names = [animal.get_name() for animal in self.__animals]
        return {
            "enclosure_id": self.__enclosure_id,
            "size": self.__size,
            "environment": self.__environment_type,
            "cleanliness": self.__cleanliness,
            "animal_count": animal_count,
            "animals": animal_names
        }

    def __str__(self):
        animal_count = len(self.__animals)
        return f"Enclosure {self.__enclosure_id} ({self.__environment_type}, {self.__size}): {animal_count} animals, Cleanliness: {self.__cleanliness}/10"

    def __eq__(self, other):
        return isinstance(other, Enclosure) and self.__enclosure_id == other.__enclosure_id