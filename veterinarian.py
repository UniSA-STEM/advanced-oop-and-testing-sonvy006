from staff import Staff

class Veterinarian(Staff):
    def __init__(self, staff_id, name, specialization):
        super().__init__(staff_id, name, "Veterinarian")
        self.__specialization = specialization

