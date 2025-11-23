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
        return isinstance(other, Animal) and self.__animal__id == other.__animal__id

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

class Bird(Animal):
    def __init__(self, name, animal_id, age, species, dietary_needs, wing_span):
        super().__init__(name, animal_id, age, species, dietary_needs)
        self.__wing_span = wing_span

    def get_wing_span(self):
        return self.__wing_span

    def set_wing_span(self, wing_span):
        if wing_span < 0:
            raise ValueError("Wing span cannot be negative")
        self.__wing_span = wing_span

    def make_sound(self):
        if "parrot" in self.get_species().lower():
            return f"{self.get_name()} squawks: 'Hello!'"
        elif "eagle" in self.get_species().lower():
            return f"{self.get_name()} screeches!"
        else:
            return f"{self.get_name()} makes a chirping sound."

    def eat(self):
        return f"{self.get_name()} eats {self.get_dietary_needs()}."

    def fly(self):
        if "penguin" in self.get_species().lower():
            return f"{self.get_name()} cannot fly but can swim!"
        else:
            return f"{self.get_name()} spreads its {self.__wing_span}cm wings and soars!."

class Reptile(Animal):
    def__init__(self, name, animal_id, age, species, dietary_needs, scale_pattern:
        super().__init__(name, animal_id, age, species, dietary_needs)
        self.__scale_pattern = scale_pattern

    def get_scale_pattern(self):
        return self.__scale_pattern

    def set_scale_pattern(self, scale_pattern):
        self.__scale_pattern = scale_pattern

    def make_sound(self):
        if "snake" in self.get_species().lower():
            return f"{self.get_name()} hisses!"
        elif "crocodile" in self.get_species().lower():
            return f"{self.get_name()} snaps!"
        else:
            return f"{self.get_name()} makes a reptilian sound."

    def eat(self):
        return f"{self.get_name()} is consuming {self.get_dietary_needs()}."

    def bask(self):
        return f"{self.get_name()} is basking under the heat"

    def __str__(self):
        return super().__str__() + f", Scale pattern: {self.__scale_pattern}"













