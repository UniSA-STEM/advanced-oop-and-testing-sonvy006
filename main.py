"""
File: main.py
Description: Main demonstration script for the Zoo Management System.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Integrity Policy.
"""
from zoo import Zoo
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian


def main():
    print("=" * 60)
    print("WELCOME TO SIMONE'S ZOO MANAGEMENT SYSTEM")
    print("=" * 60)

    simones_zoo = Zoo(name="Simone's Zoo")

    print("-" * 60)
    print("1. CREATING ASSETS AND ASSOCIATING THEM WITH ZOO")
    print("-" * 60)

    lion = Mammal(name="Tyson", animal_id="M001", species="African Lion", age=10, dietary_needs="Raw Meat",
                  fur_colour="Golden")
    parrot = Bird(name="Traitor", animal_id="B001", species="Macaw Parrot", age=3, dietary_needs="Seeds", wing_span=50)
    snake = Reptile(name="Naagin", animal_id="R001", species="King Cobra Snake", age=4, dietary_needs="Rodents",
                    scale_pattern="Diamond")

    safari = Enclosure(enclosure_id="ZONE_A", size="Large", environment_type="Safari Park", cleanliness=8)

    keeper = Zookeeper(staff_id="S001", name="Vishesh")
    vet = Veterinarian(staff_id="S002", name="Dr. Sarah", specialization="Reptiles and Birds")

    simones_zoo.add_animal(lion)
    simones_zoo.add_animal(parrot)
    simones_zoo.add_animal(snake)
    simones_zoo.add_enclosure(safari)
    simones_zoo.add_staff(keeper)
    simones_zoo.add_staff(vet)

    print(f"Zoo initialized: {simones_zoo}")
    print(f"Created Animal Instances: {lion.get_name()}, {parrot.get_name()}, {snake.get_name()}")
    print("-" * 60)

    print("2. ASSOCIATING AND HOUSING")
    print("-" * 60)

    try:
        safari.add_animal(lion)
        print(f"Housed {lion.get_name()} in {safari.get_enclosure_id()}")
    except ValueError as e:
        print(f"Error housing animal: {e}")

    keeper.assign_animal(lion)
    keeper.assign_enclosure(safari)
    vet.assign_animal(snake)
    print(f"Staff Assigned: {keeper.get_name()} and {vet.get_name()}")
    print("-" * 60)

    print("3. DEMONSTRATE POLYMORPHISM (Animal Behaviors)")
    all_animals = simones_zoo.get_animals()
    for animal in all_animals:
        print(f" - {animal.get_name()}: {animal.make_sound()}")

    print("-" * 60)

    print("4. DAILY ROUTINE (Feeding & Cleaning)")

    print(f"Action: {keeper.feed_animal(lion)}")

    print(f"Action: {keeper.clean_enclosure(safari)}")

    print("-" * 60)

    print("5. HEALTH SYSTEM INTEGRATION (Recording and Treatment)")

    print(vet.conduct_health_check(snake, issue_description="Scale infection", severity="High"))

    snakes_records = snake.get_health_records()
    print(f"Current Records for {snake.get_name()} (Count: {len(snakes_records)}):")
    print(snakes_records[0])

    print(vet.treat_animal(snakes_records[0]))

    print(f"Record Status After Treatment: {'Resolved' if snakes_records[0].is_resolved() else 'Active'}")

    print("-" * 60)

    print("6. ZOO & ENCLOSURE STATUS REPORTS")

    mammal_list = simones_zoo.get_animals_by_species("Mammal")
    print(f"Animals by Mammal species: {len(mammal_list)}")

    status = safari.get_status()
    print(
        f"Enclosure Report {status['enclosure_id']}: Animals: {status['animal_count']}, Cleanliness: {status['cleanliness']}")

    print("=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)

main()

