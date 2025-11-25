"""
File: bird.py
Description: Defines the Bird subclass, inheriting from Animal, with unique attributes and behaviors.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Bird(Animal):
    """
    Bird subclass with wing span attribute and a fly method.
    """
    def __init__(self, name, animal_id, age, species, dietary_needs, wing_span):
        """
        Initialises the Bird subclass and adds wing span.
        :param name: name of the animal
        :param animal_id: unique identifier of the animal
        :param age: age of the animal in years
        :param species: species of the animal
        :param dietary_needs: description of the dietary needs
        :param wing_span: length of the wing span in cm.
        """
        super().__init__(name, animal_id, age, species, dietary_needs)
        self.__wing_span = wing_span

    def get_wing_span(self):
        """
        Returns the wing span of the bird.
        :return: integer wing span of the bird.
        """
        return self.__wing_span

    def set_wing_span(self, wing_span):
        """
        Sets the wing span of the bird.
        :param wing_span: new wing span of the bird.
        :return: None
        """
        if wing_span < 0:
            raise ValueError("Wing span cannot be negative")
        self.__wing_span = wing_span

    def make_sound(self):
        """
        Overrides the abstract with specific bird sounds.
        :return: string
        """
        if "parrot" in self.get_species().lower():
            return f"{self.get_name()} squawks: 'Hello!'"
        elif "eagle" in self.get_species().lower():
            return f"{self.get_name()} screeches!"
        else:
            return f"{self.get_name()} makes a chirping sound."

    def eat(self):
        """
        Overrides the abstract with specific bird eating description.
        :return: string
        """
        return f"{self.get_name()} eats {self.get_dietary_needs()}."

    def fly(self):
        """
        Overrides the abstract with specific bird flying capability.
        :return: string description of birds movement.
        """
        if "penguin" in self.get_species().lower():
            return f"{self.get_name()} cannot fly but can swim!"
        else:
            return f"{self.get_name()} spreads its {self.__wing_span}cm wings and soars!."