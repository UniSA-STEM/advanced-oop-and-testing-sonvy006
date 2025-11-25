"""
File: test_animal.py
Description: The unit test file for Animal classes.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""
import pytest
from mammal import Mammal
from bird import Bird
from reptile import Reptile


class TestMammal:
    """
    Tests Mammal specific attributes, methods, and validation logic
    """
    @pytest.fixture
    def lion(self):
        return Mammal(name="Tyson", animal_id="M001", species="Lion", age=10, dietary_needs="Meat", fur_colour="Golden")

    def test_mammal_creation(self, lion):
        assert lion.get_name() == "Tyson"
        assert lion.get_species() == "Lion"
        assert lion.get_age() == 10
        assert lion.get_fur_colour() == "Golden"

    def test_mammal_make_sound(self, lion):
        sound = lion.make_sound()
        assert "Tyson" in sound
        assert "roar" in sound.lower()

    def test_mammal_eat(self, lion):
        result = lion.eat()
        assert "eats" in result.lower()

    def test_set_age_valid(self, lion):
        lion.set_age(6)
        assert lion.get_age() == 6

    def test_set_age_invalid(self, lion):
        with pytest.raises(ValueError):
            lion.set_age(-1)

    def test_mammal_equality(self):
        lion1 = Mammal(name="Tyson", animal_id="M001", species="Lion", age=10, dietary_needs="Meat", fur_colour="Golden")
        lion2 = Mammal(name="Different", animal_id="M001", species="Lion", age=3, dietary_needs="Meat", fur_colour="Brown")
        lion3 = Mammal(name="Tyson", animal_id="M002", species="Lion", age=10, dietary_needs="Meat", fur_colour="Golden")

        assert lion1 == lion2
        assert lion1 != lion3


class TestBird:
    """
    Tests bird specific attributes, methods, and validation logic
    """
    @pytest.fixture
    def parrot(self):
        return Bird(name="Traitor", animal_id="B001", species="Parrot", age=3, dietary_needs="Seeds", wing_span=95)

    def test_bird_creation(self, parrot):
        assert parrot.get_name() == "Traitor"
        assert parrot.get_wing_span() == 95

    def test_bird_make_sound(self, parrot):
        sound = parrot.make_sound()
        assert "Traitor" in sound

    def test_set_wing_span_invalid(self, parrot):
        with pytest.raises(ValueError):
            parrot.set_wing_span(-10)


class TestReptile:
    """
    Tests reptile specific attributes, methods, and validation logic
    """
    @pytest.fixture
    def snake(self):
        return Reptile(name="Naagin", animal_id="R001", species="Python Snake", age=4, dietary_needs="Rodents", scale_pattern="Diamond")

    def test_reptile_creation(self, snake):
        assert snake.get_name() == "Naagin"
        assert snake.get_scale_pattern() == "Diamond"

    def test_reptile_make_sound(self, snake):
        sound = snake.make_sound()
        assert "hiss" in sound.lower()