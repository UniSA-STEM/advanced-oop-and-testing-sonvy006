from staff import Staff

class Veterinarian(Staff):
    def __init__(self, staff_id, name, specialization):
        super().__init__(staff_id, name, "Veterinarian")
        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def perform_duty(self):
        return f"Dr. {self.get_name()} is performing duties: conducting health checks"

    def conduct_health_check(self, animal):
        if animal not in self.get_assigned_animals():
            raise ValueError(f"The {animal.get_name()} is not assigned to Dr. {self.get_name()}.")
        return f"Dr. {self.get_name()} examined {animal.get_name()} is looking healthy!"

    def __str__(self):
        animal_count = len(self.get_assigned_animals())
        return super().__str__() + f" (Specialization: {self.__specialization}) - Caring for {animal_count} animals"

