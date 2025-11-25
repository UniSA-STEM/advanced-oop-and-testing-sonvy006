"""
File: zookeeper.py
Description: Defines the Zookeeper subclass, specializing in routine animal and enclosure care.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff

class Zookeeper(Staff):
    """
    Subclass of Zookeeper with their specialise in routine care,
    including feeding animals and cleaning enclosures.
    Inherits from Staff.
    """
    def __init__(self, staff_id, name):
        """
        Initializes the Zookeeper subclass.
        :param staff_id: unique identifier for the Zookeeper staff.
        :param name: name of the Zookeeper staff.
        """
        super().__init__(staff_id, name,"Zookeeper")

    def perform_duty(self):
        """
        Overrides the abstract method in Staff with perfom_duty method.
        :return: string
        """
        return f"{self.get_name()} is performing their duties: feeding and caring for animals."

    def feed_animal(self, animal):
        """
        Feeds a specific animal, and
        checking if the animal is assigned to this zookeeper.
        :param animal: animal object to feed
        :return: string
        """
        if animal not in self.get_assigned_animals():
            raise ValueError(f"{animal.get_name()} is not assigned to {self.get_name()}.")
        return f"{self.get_name()} is feeding {animal.get_name()}: {animal.eat()}"

    def clean_enclosure(self, enclosure):
        """
        Cleans the enclosure care, and setting level to maximum of cleanliness
        :param enclosure: enclosure object to clean
        :return: string
        """
        if enclosure not in self.get_assigned_enclosures():
            raise ValueError(f"Enclosure {enclosure.get_enclosure_id()} is not assigned to {self.get_name()}.")

        enclosure.set_cleanliness(10)
        return f"{self.get_name()} has cleaned enclosure {enclosure.get_enclosure_id()}. Cleanliness is now at top!"

    def __str__(self):
        """
        Overall representation including the number of animals and enclosures.
        :return: Staff summary
        """
        animal_count = len(self.get_assigned_animals())
        enclosure_count = len(self.get_assigned_enclosures())
        return super().__str__() + f" - Caring for {animal_count} animals in {enclosure_count} enclosures"



