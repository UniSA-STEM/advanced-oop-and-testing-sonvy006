"""
File: reptile.py
Description: Defines the Reptile subclass, inheriting from Animal, with unique attributes and behaviors.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Reptile(Animal):
    """
    Subclass of Reptile including scale pattern and implementing abstract method.
    """
    def __init__(self, name, animal_id, age, species, dietary_needs, scale_pattern):
        """
        Initialises the Reptile class.
        :param name: name of the animal.
        :param animal_id: unique identifier of the animal.
        :param age: age of the animal in years.
        :param species: species of the animal.
        :param dietary_needs: dietary needs of the animal.
        :param scale_pattern: reptile's scale_pattern attribute.
        """
        super().__init__(name, animal_id, age, species, dietary_needs)
        self.__scale_pattern = scale_pattern

    def get_scale_pattern(self):
        """
        Returns the scale pattern of the animal.
        :return: string representing the scale pattern.
        """
        return self.__scale_pattern

    def set_scale_pattern(self, scale_pattern):
        """
        Sets the scale pattern of the animal.
        :param scale_pattern: new scale pattern.
        :return: None
        """
        self.__scale_pattern = scale_pattern

    def make_sound(self):
        """
        Overrides the abstract method with specific reptile sounds.
        :return: string description of sounds.
        """
        if "snake" in self.get_species().lower():
            return f"{self.get_name()} hisses!"
        elif "crocodile" in self.get_species().lower():
            return f"{self.get_name()} snaps!"
        else:
            return f"{self.get_name()} makes a reptilian sound."

    def eat(self):
        """
        Overrides the abstract method with specific reptile eats.
        :return: string description of eats.
        """
        return f"{self.get_name()} is consuming {self.get_dietary_needs()}."

    def bask(self):
        """
        Overrides the abstract method with specific reptile basks.
        :return: string describing basking action.
        """
        return f"{self.get_name()} is basking under the heat"

    def __str__(self):
        """
        String representation with including scale pattern.
        :return: Reptile's summary with scale pattern.
        """
        return super().__str__() + f", Scale pattern: {self.__scale_pattern}"

