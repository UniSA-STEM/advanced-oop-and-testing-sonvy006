"""
File: health_record.py
Description: Health Record of the animals.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""
class HealthRecord:
    """
    class representing a single health event or issue for an animal.
    """
    def __init__(self, record_id, animal, issue_description, severity):
        """
        Initialise the health record.
        :param record_id: unique record ID.
        :param animal: animal object.
        :param issue_description: description of the issue.
        :param severity: severity of the issue.
        """
        self.__record_id = record_id
        self.__animal = animal
        self.__issue_description = issue_description
        self.__severity = severity
        self.__resolved = False

    def get_record_id(self):
        return self.__record_id

    def get_animal(self):
        return self.__animal

    def get_issue_description(self):
        return self.__issue_description

    def set_issue_description(self, issue_description):
        self.__issue_description = issue_description

    def get_severity(self):
        return self.__severity

    def set_severity(self, severity):
        """
        Set the severity of the issue.
        :param severity: new severity of the issue. string
        :return: None
        """
        valid_severities = ["low", "medium", "high", "critical"]
        if severity.lower() not in valid_severities:
            raise ValueError(f"Severity must be one of: {', '.join(valid_severities)}")
        self.__severity = severity.lower()

    def is_resolved(self):
        return self.__resolved

    def resolve(self):
        self.__resolved = True

    def __str__(self):
        """
        Returns a formatted summary of the health record status and issue.
        """
        status = "Resolved" if self.__resolved else "Active"
        return (f"Health Record #{self.__record_id} - {self.__animal.get_name()}\n"
                f"Issue: {self.__issue_description}\n"
                f"Severity: {self.__severity.upper()}\n"
                f"Status: {status}")

    def __eq__(self, other):
        """
        Checks if two health records are equal based on their record ID.
        :param other: object to compare.
        :return: true if both objects are equal, false otherwise.
        """
        return isinstance(other, HealthRecord) and self.__record_id == other.__record_id