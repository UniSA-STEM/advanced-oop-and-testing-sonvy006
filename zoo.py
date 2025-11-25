"""
File: zoo.py
Description: The main management hub for the zoo. Handles all top-level operations and asset aggregation.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Zoo:
    """
    main management hub for the zoo.
    """
    def __init__(self, name):
        """
        Initializes the Zoo, setting its name and creating empty lists for all aggregated assets.
        :param name: The name of the zoo (str).
        """
        self.__name = name
        self.__animals = []
        self.__enclosures = []
        self.__staff = []

    def get_name(self):
        """
        Returns the name of the zoo (str).
        """
        return self.__name

    def get_animals(self):
        """
        Returns the list of all animals in the zoo (list).
        """
        return self.__animals

    def get_enclosures(self):
        """
        return the list of all enclosures in the zoo (list).
        """
        return self.__enclosures

    def get_staff(self):
        """
        Returns the list of all staffs in the zoo (list).
        """
        return self.__staff

    def add_animal(self, animal):
        if animal in self.__animals:
            raise ValueError(f"{animal.get_name()} is already in the zoo.")
        self.__animals.append(animal)

    def remove_animal(self, animal):
        if animal not in self.__animals:
            raise ValueError(f"{animal.get_name()} is not in the zoo.")
        self.__animals.remove(animal)

    def add_enclosure(self, enclosure):
        """
        Adds an enclosure to the zoo, checking for duplicates.
        """
        if enclosure in self.__enclosures:
            raise ValueError(f"Enclosure {enclosure.get_enclosure_id()} already exists.")
        self.__enclosures.append(enclosure)

    def remove_enclosure(self, enclosure):
        """
        Removes an enclosure from the zoo, checking for duplicates.
        """
        if enclosure not in self.__enclosures:
            raise ValueError(f"Enclosure {enclosure.get_enclosure_id()} does not exist.")

        if len(enclosure.get_animals()) > 0:
            raise ValueError(f"Cannot remove enclosure with animals inside.")

        self.__enclosures.remove(enclosure)

    def add_staff(self, staff_member):
        if staff_member in self.__staff:
            raise ValueError(f"{staff_member.get_name()} is already employed.")
        self.__staff.append(staff_member)

    def remove_staff(self, staff_member):
        if staff_member not in self.__staff:
            raise ValueError(f"{staff_member.get_name()} is not employed here.")
        self.__staff.remove(staff_member)

    def get_animals_by_species(self, species):
        """
        Generates a list of animals filtered by their class type (e.g., Mammal, Bird).
        :return: List of Animal objects matching the class type (list).
        """
        return [animal for animal in self.__animals if species.lower() in animal.get_species().lower()]

    def __str__(self):
        """
        Returns a summary of the zoo's current occupancy.
        :return: Zoo status summary (str).
        """
        return (f"{self.__name}\n"
                f"Animals: {len(self.__animals)}\n"
                f"Enclosures: {len(self.__enclosures)}\n"
                f"Staff: {len(self.__staff)}")

