"""
File: test_health_record.py
Description: Unit tests for HealthRecord class.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""
import pytest
from health_record import HealthRecord
from mammal import Mammal


class TestHealthRecord:

    @pytest.fixture
    def lion(self):
        return Mammal(name="Tyson", animal_id="M001", species="Lion", age=10, dietary_needs="Meat", fur_colour="Golden")

    @pytest.fixture
    def record(self, lion):
        return HealthRecord(record_id="HR-001", animal=lion, issue_description="Sore paw", severity="low")

    def test_record_creation(self, record, lion):
        assert record.get_record_id() == "HR-001"
        assert record.get_animal() == lion
        assert record.get_issue_description() == "Sore paw"
        assert record.get_severity() == "low"
        assert record.is_resolved() is False

    def test_set_issue_description(self, record):
        record.set_issue_description("Infected cut")
        assert record.get_issue_description() == "Infected cut"

    def test_set_severity_valid(self, record):
        record.set_severity("Critical")
        assert record.get_severity() == "critical"

    def test_set_severity_invalid(self, record):
        with pytest.raises(ValueError):
            record.set_severity("Extreme")

    def test_resolve_issue(self, record):
        assert record.is_resolved() is False
        record.resolve()
        assert record.is_resolved() is True

    def test_str_representation(self, record):
        assert "Active" in str(record)
        assert "HR-001" in str(record)
        record.resolve()
        assert "Resolved" in str(record)

    def test_equality(self, lion):
        record1 = HealthRecord(record_id="HR-001", animal=lion, issue_description="Sore paw", severity="low")
        record2 = HealthRecord(record_id="HR-001", animal=lion, issue_description="Different issue", severity="high")
        record3 = HealthRecord(record_id="HR-002", animal=lion, issue_description="Sore paw", severity="low")

        assert record1 == record2
        assert record1 != record3