"""
File: test_staff.py
Description: Unit tests for Staff classes.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""
import pytest
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from mammal import Mammal
from enclosure import Enclosure


class TestZookeeper:

    @pytest.fixture
    def keeper(self):
        return Zookeeper(staff_id="S001", name="Vishesh")

    @pytest.fixture
    def lion(self):
        return Mammal(name="Tyson", animal_id="M001", species="Lion", age=10, dietary_needs="Meat", fur_colour="Golden")

    @pytest.fixture
    def safari(self):
        return Enclosure(enclosure_id="ZONE_A", size="Large", environment_type="Safari Park", cleanliness=5)

    def test_zookeeper_creation(self, keeper):
        assert keeper.get_name() == "Vishesh"
        assert keeper.get_role() == "Zookeeper"

    def test_assign_animal(self, keeper, lion):
        keeper.assign_animal(lion)
        assert lion in keeper.get_assigned_animals()

    def test_feed_animal(self, keeper, lion):
        keeper.assign_animal(lion)
        result = keeper.feed_animal(lion)
        assert "feeding" in result.lower()
        assert "Tyson" in result

    def test_feed_unassigned_raises_error(self, keeper, lion):
        with pytest.raises(ValueError):
            keeper.feed_animal(lion)

    def test_clean_enclosure(self, keeper, safari):
        keeper.assign_enclosure(safari)
        keeper.clean_enclosure(safari)
        assert safari.get_cleanliness() == 10


class TestVeterinarian:

    @pytest.fixture
    def vet(self):
        return Veterinarian(staff_id="S002", name="Sarah", specialization="Mammals")

    @pytest.fixture
    def lion(self):
        return Mammal(name="Tyson", animal_id="M001", species="Lion", age=10, dietary_needs="Meat", fur_colour="Golden")

    def test_vet_creation(self, vet):
        assert vet.get_name() == "Sarah"
        assert vet.get_specialization() == "Mammals"

    def test_conduct_health_check_creates_record(self, vet, lion):
        vet.assign_animal(lion)

        result = vet.conduct_health_check(lion, "Sore paw", "Low")

        assert "recorded a new low health issue" in result.lower()
        assert len(lion.get_health_records()) == 1
        assert lion.get_health_records()[0].get_issue_description() == "Sore paw"

    def test_health_check_unassigned_raises_error(self, vet, lion):
        with pytest.raises(ValueError):
            vet.conduct_health_check(lion)