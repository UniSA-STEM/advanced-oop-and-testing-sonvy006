"""
File: test_enclosure.py
Description: Unit tests for Enclosure class.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""
import pytest
from enclosure import Enclosure
from mammal import Mammal
from bird import Bird


class TestEnclosure:

    @pytest.fixture
    def safari(self):
        return Enclosure(enclosure_id="ZONE_A", size="Large", environment_type="Safari Park", cleanliness=8)

    @pytest.fixture
    def lion(self):
        return Mammal(name="Tyson", animal_id="M001", species="Lion", age=10, dietary_needs="Meat", fur_colour="Golden")

    @pytest.fixture
    def elephant(self):
        return Mammal(name="Manny", animal_id="M002", species="Elephant", age=12, dietary_needs="Grass", fur_colour="Gray")

    @pytest.fixture
    def parrot(self):
        return Bird(name="Traitor", animal_id="B001", species="Parrot", age=3, dietary_needs="Seeds", wing_span=50)

    def test_enclosure_creation(self, safari):
        assert safari.get_enclosure_id() == "ZONE_A"
        assert safari.get_size() == "Large"
        assert safari.get_cleanliness() == 8

    def test_add_animal(self, safari, lion):
        safari.add_animal(lion)
        assert lion in safari.get_animals()

    def test_add_multiple_same_type(self, safari, lion, elephant):
        safari.add_animal(lion)
        safari.add_animal(elephant)
        assert len(safari.get_animals()) == 2

    def test_add_different_type_raises_error(self, safari, lion, parrot):
        safari.add_animal(lion)
        with pytest.raises(ValueError):
            safari.add_animal(parrot)

    def test_add_duplicate_raises_error(self, safari, lion):
        safari.add_animal(lion)
        with pytest.raises(ValueError):
            safari.add_animal(lion)

    def test_remove_animal(self, safari, lion):
        safari.add_animal(lion)
        safari.remove_animal(lion)
        assert lion not in safari.get_animals()

    def test_set_cleanliness_valid(self, safari):
        safari.set_cleanliness(10)
        assert safari.get_cleanliness() == 10

    def test_set_cleanliness_invalid(self, safari):
        with pytest.raises(ValueError):
            safari.set_cleanliness(11)

    def test_get_status(self, safari, lion):
        safari.add_animal(lion)
        status = safari.get_status()

        assert status["enclosure_id"] == "ZONE_A"
        assert status["animal_count"] == 1
        assert "Tyson" in status["animals"]