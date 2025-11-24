from staff import Staff

class Zookeeper(Staff):

    def __init__(self, staff_id, name):
        super().__init__(staff_id, name,"Zookeeper")

    def perform_duty(self):
        return f"{self.get_name()} is performing their duties: feeding and caring for animals."

    def feed_animal(self, animal):
        if animal not in self.get_assigned_animals():
            raise ValueError(f"{animal.get_name()} is not assigned to {self.get_name()}.")
        return f"{self.get_name()} is feeding {animal.get_name()}: {animal.eat()}"

    def clean_enclosure(self, enclosure):
        if enclosure not in self.get_assigned_enclosures():
            raise ValueError(f"Enclosure {enclosure.get_enclosure_id()} is not assigned to {self.get_name()}.")

        enclosure.set_cleanliness(10)
        return f"{self.get_name()} has cleaned enclosure {enclosure.get_enclosure_id()}. Cleanliness is now at top!"

    def __str__(self):
        animal_count = len(self.get_assigned_animals())
        enclosure_count = len(self.get_assigned_enclosures())
        return super().__str__() + f" - Caring for {animal_count} animals in {enclosure_count} enclosures"



