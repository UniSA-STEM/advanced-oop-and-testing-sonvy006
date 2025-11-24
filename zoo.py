class Zoo:
    def __init__(self, name):
        self.__name = name
        self.__animals = []
        self.__enclosures = []
        self.__staff = []

    def get_name(self):
        return self.__name

    def get_animals(self):
        return self.__animals

    def get_enclosures(self):
        return self.__enclosures

    def get_staff(self):
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
        if enclosure in self.__enclosures:
            raise ValueError(f"Enclosure {enclosure.get_enclosure_id()} already exists.")
        self.__enclosures.append(enclosure)

    def remove_enclosure(self, enclosure):
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
        return [animal for animal in self.__animals if species.lower() in animal.get_species().lower()]

    def __str__(self):
        return (f"{self.__name}\n"
                f"Animals: {len(self.__animals)}\n"
                f"Enclosures: {len(self.__enclosures)}\n"
                f"Staff: {len(self.__staff)}")
