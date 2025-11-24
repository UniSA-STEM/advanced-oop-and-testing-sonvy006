from animal import Animal

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