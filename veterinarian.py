from staff import Staff
from health_record import HealthRecord

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

    def conduct_health_check(self, animal, issue_description=None, severity=None):
        if animal not in self.get_assigned_animals():
            raise ValueError(f"{animal.get_name()} is not assigned to Dr. {self.get_name()}.")

        if issue_description and severity:
            record_id = f"HR - {len(animal.get_health_records()) + 1:03d}"
            new_record = HealthRecord(record_id, animal, issue_description, severity)
            animal.add_health_record(new_record)
            return f"Dr. {self.get_name()} recorded a new {severity} health issue for {animal.get_name()}: {issue_description}"
        else:
            active_issues = [record for record in animal.get_health_records() if not record.is_resolved()]
            if len(active_issues) > 0:
                return f"Dr. {self.get_name()} examined {animal.get_name()} and found {len(active_issues)} active health issue(s)."
            else:
                return f"Dr. {self.get_name()} examined {animal.get_name()} - clean bill of health!"

    def treat_animal(self, health_record):
        animal = health_record.get_animal()

        if animal not in self.get_assigned_animals():
            raise ValueError(f"{animal.get_name()} is not assigned to Dr. {self.get_name()}.")

        if health_record.is_resolved():
            return f"Health issue for {animal.get_name()} is already resolved."

        health_record.resolve()
        return f"Dr. {self.get_name()} successfully treated {animal.get_name()} for: {health_record.get_issue_description()}"

    def __str__(self):
        animal_count = len(self.get_assigned_animals())
        return super().__str__() + f" (Specialization: {self.__specialization}) - Caring for {animal_count} animals"