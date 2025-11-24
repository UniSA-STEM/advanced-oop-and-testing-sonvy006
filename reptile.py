from animal import Animal

class Reptile(Animal):
    def __init__(self, name, animal_id, age, species, dietary_needs, scale_pattern):
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

