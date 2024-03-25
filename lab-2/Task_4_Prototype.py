import copy

class Virus:
    def __init__(self, weight, age, name, species):
        self.weight = weight
        self.age = age
        self.name = name
        self.species = species
        self.children = []

    def add_child(self, child_virus):
        if isinstance(child_virus, Virus):
            self.children.append(child_virus)
        else:
            print("Child must be an instance of Virus.")

    def clone(self):
        cloned_virus = copy.deepcopy(self)
        cloned_virus.children = [child.clone() for child in self.children]
        return cloned_virus

    def __str__(self):
        return f"Name: {self.name}, Weight: {self.weight}, Age: {self.age}, Species: {self.species}"

# Приклад використання
if __name__ == "__main__":

    # Створення батьківського вірусу
    virus1 = Virus(0.1, 1, "COVID-19", "Coronavirus")

    # Додавання дітей до батьківського вірусу
    virus2 = Virus(0.08, 2, "Influenza", "Orthomyxovirus")
    virus3 = Virus(0.05, 3, "Ebola", "Filovirus")
    virus1.add_child(virus2)
    virus1.add_child(virus3)

    # Клонування вірусу-батька
    cloned_virus = virus1.clone()

    # Виведення клонованих вірусів
    print("Original Virus:")
    print(virus1)

    print("\nCloned Virus:")
    print(cloned_virus)

    print("\nChildren of Cloned Virus:")
    for child in cloned_virus.children:
        print(child)