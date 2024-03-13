class ZooManager:
    def __init__(self, name):
        self.name = name
        self.enclosures = []

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def display_all_enclosures(self):
        print("All Enclosures:")
        for enclosure in self.enclosures:
            print(f"{enclosure.enclosure_type} enclosure - Size: {enclosure.size}")

    def feed_all_animals(self, food):
        print(f"{self.name} is feeding all animals with {food}.")
        for enclosure in self.enclosures:
            for animal in enclosure.animals:
                animal.feed(food)

    def organize_event(self, event_name, participants):
        print(f"{self.name} is organizing an event: {event_name}")
        print("Participants:")
        for participant in participants:
            if isinstance(participant, Animal):
                print(f" - {participant.name} ({participant.species})")
            elif isinstance(participant, ZooKeeper):
                print(f" - {participant.name} ({participant.role})")

    def display_monthly_statistics(self):
        print("Monthly Statistics:")


class MonthlyStatistics:
    def __init__(self):
        self.feedings_count = 0
        self.keeper_interactions_count = 0

    def record_feeding(self):
        self.feedings_count += 1

    def record_keeper_interaction(self):
        self.keeper_interactions_count += 1

    def display_statistics(self):
        print("Monthly Statistics:")
        self._display_count("Number of feedings", self.feedings_count)
        self._display_count("Number of keeper interactions", self.keeper_interactions_count)

    def _display_count(self, label, count):
        print(f"{label}: {count}")


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def feed(self, food):
        print(f"{self.name} is eating {food}.")

    def display_monthly_statistics(self):
        print("Monthly Statistics:")
        monthly_stats = MonthlyStatistics()
        for enclosure in self.enclosures:
            for animal in enclosure.animals:
                monthly_stats.record_feeding(animal.get_events_count())
        monthly_stats.display_statistics()

class Enclosure:
    def __init__(self, size, enclosure_type):
        self.size = size
        self.enclosure_type = enclosure_type
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

class ZooKeeper:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def feed_animal(self, animal, food):
        print(f"{self.name} is feeding {animal.name} with {food}.")
        animal.feed(food)

class Feeding:
    def feed_animal(self, animal, food):
        print(f"{self.name} is feeding {animal.name} with {food}.")
        animal.feed(food)

class Inventory:
    def display_animals(self, enclosure):
        print(f"Animals in {enclosure.enclosure_type} enclosure:")
        for animal in enclosure.animals:
            print(f"{animal.name} - {animal.species}")

    def display_employees(self, employees):
        print("Zoo Employees:")
        for employee in employees:
            print(f"{employee.name} - {employee.role}")


        self._display_count("Number of employees", len(employees))

    def _display_count(self, label, count):
        print(f"{label}: {count}")