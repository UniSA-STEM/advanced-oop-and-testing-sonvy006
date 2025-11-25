"""
File: animal.py
Description: Establishes the abstract class for all zoo animals.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class for all zoo animals.
    It shows fundamental properties and behaviours of all the zoo animals.
    """
    def __init__(self, name, animal_id, age, species, dietary_needs):
        """
        Initialises the animal's attributes.
        :param name: the name of the animal
        :param animal_id: a unique identifier of the animal (eg: M001.)
        :param age: age of the animal in years
        :param species: species of the animal
        :param dietary_needs: a description of the animal's dietary needs
        """
        self.__name = name
        self.__animal_id = animal_id
        self.__age = age
        self.__species = species
        self.__dietary_needs = dietary_needs
        self.__health_records = []

    def get_animal_id(self):
        """
        Returns the animal's unique identifier.
        :return: animal's ID
        """
        return self.__animal_id

    def get_name(self):
        """
        Returns the animal's name.
        :return: animal's name (string)
        """
        return self.__name

    def get_age(self):
        """
        Returns the animal's age in years.
        :return: integer
        """
        return self.__age

    def get_species(self):
        """
        Returns the animal's species.
        :return: animal's species (string)
        """
        return self.__species

    def get_dietary_needs(self):
        """
        Returns the animal's dietary needs/requirements.
        :return: string or None
        """
        return self.__dietary_needs

    def set_age(self, age):
        """
        Sets the animal's age after validating it is not negative.
        :param age: new age of the animal
        :return: None
        """
        if age < 0:
            raise ValueError('Age cannot be negative')
        self.__age = age

    def set_dietary_needs(self, dietary_needs):
        """
        Sets the animal's dietary needs/requirements.
        :param dietary_needs: new dietary needs (string)
        :return: None
        """
        self.__dietary_needs = dietary_needs

    def get_health_records(self):
        """
        Returns the list of health records for the animal.
        :return: list of health records
        """
        return self.__health_records

    def add_health_record(self, health_record):
        """
        Adds a new health record to the list.
        :param health_record: The health record to be added
        :return: None
        """
        self.__health_records.append(health_record)

    @abstractmethod
    def make_sound(self):
        """
        Using abstract methods to make a sound.
        :return: string describing the sound
        """
        pass

    @abstractmethod
    def eat(self):
        """
        Using abstract methods to define eating behaviour.
        :return: String describing the eating behaviour
        """
        pass

    def sleep(self):
        """
        Returns a string describing the sleep behaviour.
        """
        return f"{self.__name} is peacefully sleeping."

    def __str__(self):
        """
        human readable string description of the animal.
        :return: animal summary (string)
        """
        return f"{self.__name} ({self.__species}), Age: {self.__age}"

    def __eq__(self, other):
        """
        Checks if two animals are equal.
        :param other: The other object to compare to.
        :return: True if ID's are the same, False otherwise.
        """
        return isinstance(other, Animal) and self.__animal_id == other.__animal_id









