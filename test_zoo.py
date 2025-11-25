"""
File: test_zoo.py
Description: Unit tests for Zoo class.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""
import pytest
from zoo import Zoo
from mammal import Mammal
from bird import Bird
from enclosure import Enclosure
from zookeeper import Zookeeper


class TestZoo:
    """
    Tests the main Zoo management hub, covering aggregation lists and filtering.
    """
    @pytest.fixture
    def zoo(self):
        return Zoo(name="Simone's Zoo")

    @pytest.fixture
    def lion(self):
        return Mammal(name="Tyson", animal_id="M001", species="Lion", age=10, dietary_needs="Meat", fur_colour="Golden")

    @pytest.fixture
    def parrot(self):
        return Bird(name="Traitor", animal_id="B001", species="Parrot", age=3, dietary_needs="Seeds", wing_span=50)

    @pytest.fixture
    def safari(self):
        return Enclosure(enclosure_id="ZONE_A", size="Large", environment_type="Safari Park", cleanliness=8)

    @pytest.fixture
    def keeper(self):
        return Zookeeper(staff_id="S001", name="Vishesh")

    def test_zoo_creation(self, zoo):
        assert zoo.get_name() == "Simone's Zoo"
        assert len(zoo.get_animals()) == 0
        assert len(zoo.get_enclosures()) == 0
        assert len(zoo.get_staff()) == 0

    def test_add_animal(self, zoo, lion):
        zoo.add_animal(lion)
        assert lion in zoo.get_animals()
        assert len(zoo.get_animals()) == 1

    def test_add_duplicate_animal_raises_error(self, zoo, lion):
        zoo.add_animal(lion)
        with pytest.raises(ValueError):
            zoo.add_animal(lion)

    def test_remove_animal(self, zoo, lion):
        zoo.add_animal(lion)
        zoo.remove_animal(lion)
        assert lion not in zoo.get_animals()
        assert len(zoo.get_animals()) == 0

    def test_remove_missing_animal_raises_error(self, zoo, lion):
        with pytest.raises(ValueError):
            zoo.remove_animal(lion)

    def test_add_enclosure(self, zoo, safari):
        zoo.add_enclosure(safari)
        assert safari in zoo.get_enclosures()

    def test_add_duplicate_enclosure_raises_error(self, zoo, safari):
        zoo.add_enclosure(safari)
        with pytest.raises(ValueError):
            zoo.add_enclosure(safari)

    def test_remove_enclosure(self, zoo, safari):
        zoo.add_enclosure(safari)
        zoo.remove_enclosure(safari)
        assert safari not in zoo.get_enclosures()

    def test_remove_enclosure_with_animals_raises_error(self, zoo, safari, lion):
        safari.add_animal(lion)
        zoo.add_enclosure(safari)

        with pytest.raises(ValueError):
            zoo.remove_enclosure(safari)

    def test_add_staff(self, zoo, keeper):
        zoo.add_staff(keeper)
        assert keeper in zoo.get_staff()

    def test_remove_staff(self, zoo, keeper):
        zoo.add_staff(keeper)
        zoo.remove_staff(keeper)
        assert keeper not in zoo.get_staff()

    def test_get_animals_by_species(self, zoo, lion, parrot):
        zoo.add_animal(lion)
        zoo.add_animal(parrot)

        lions = zoo.get_animals_by_species("Lion")

        assert len(lions) == 1
        assert lion in lions
        assert parrot not in lions