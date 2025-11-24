class HealthRecord:
    def __init__(self, record_id, animal, issue_description, severity):
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
        valid_severities = ["low", "medium", "high", "critical"]
        if severity.lower() not in valid_severities:
            raise ValueError(f"Severity must be one of: {', '.join(valid_severities)}")
        self.__severity = severity.lower()

    def is_resolved(self):
        return self.__resolved

    def resolve(self):
        self.__resolved = True

    def __str__(self):
        status = "Resolved" if self.__resolved else "Active"
        return (f"Health Record #{self.__record_id} - {self.__animal.get_name()}\n"
                f"Issue: {self.__issue_description}\n"
                f"Severity: {self.__severity.upper()}\n"
                f"Status: {status}")

    def __eq__(self, other):
        return isinstance(other, HealthRecord) and self.__record_id == other.__record_id