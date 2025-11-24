class HealthRecord:
    def __init__(self, record_id, animal, issue_description, severity):
        self.__record_id = record_id
        self.__animal = animal
        self.__issue_description = issue_description
        self.__severity = severity
        self.__resolved = False