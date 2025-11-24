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
    def __init__(self, name, animal_id, age, species, dietary_needs, fur_colour):
        super().__init__(name, animal_id, age, species, dietary_needs)
        self.__fur_colour = fur_colour

    def get_fur_colour(self):
        return self.__fur_colour

    def set_fur_colour(self, fur_colour):
        self.__fur_colour = fur_colour

    def make_sound(self):
        if "lion" in self.get_species().lower():
            return f"{self.get_name()} does roars loudly."
        elif "elephant" in self.get_species().lower():
            return f"{self.get_name()} trumpets loudly with its trunk."
        else:
            return f"{self.get_name()} does make a mammal sound."

    def eat(self):
        return f"{self.get_name()} eats {self.get_dietary_needs()}."

    def __str__(self):
        return super().__str__() + f", Fur colour: {self.__fur_colour}"
