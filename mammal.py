"""
File: mammal.py
Description: A description of mammal file.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Mammal(Animal):
    """
    Subclass of Mammal, including a fur colour attribute and
    implementing abstract methods.
    """
    def __init__(self, name, animal_id, age, species, dietary_needs, fur_colour):
        """
        Initialises the Mammal object.
        :param name: the animal name
        :param animal_id: unique identifier of the animal
        :param age: age of the animal in years
        :param species: species of the animal
        :param dietary_needs: description of the dietary needs
        :param fur_colour: colour of the fur
        """
        super().__init__(name, animal_id, age, species, dietary_needs)
        self.__fur_colour = fur_colour

    def get_fur_colour(self):
        """
        Returns the fur colour of the animal.
        :return: string
        """
        return self.__fur_colour

    def set_fur_colour(self, fur_colour):
        """
        Sets the fur colour of the animal.
        :param fur_colour: new fur colour
        :return: None
        """
        self.__fur_colour = fur_colour

    def make_sound(self):
        """
        Overrides the abstract method of the Animal class with specific mammal sounds.
        :return: string describing the sound of the species.
        """
        if "lion" in self.get_species().lower():
            return f"{self.get_name()} does roars loudly."
        elif "elephant" in self.get_species().lower():
            return f"{self.get_name()} trumpets loudly with its trunk."
        else:
            return f"{self.get_name()} does make a mammal sound."

    def eat(self):
        """
        Overrides the abstract eat method with eating description of mammal.
        :return: string describing mammals eating.
        """
        return f"{self.get_name()} eats {self.get_dietary_needs()}."

    def __str__(self):
        """
        Includes fur colour into string representation
        :return: mammal summary with fur colour
        """
        return super().__str__() + f", Fur colour: {self.__fur_colour}"
