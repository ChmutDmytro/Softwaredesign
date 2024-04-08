# Класи героїв
class Warrior:
    def __init__(self, name):
        self.name = name

class Mage:
    def __init__(self, name):
        self.name = name

class Paladin:
    def __init__(self, name):
        self.name = name


class Inventory:
    def __init__(self, hero):
        self.hero = hero
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_inventory(self):
        return [item for item in self.items]

class Clothing:
    def __init__(self, name):
        self.name = name

class Weapon:
    def __init__(self, name):
        self.name = name

class Artifact:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    # Створення героїв
    warrior = Warrior("Warrior")
    mage = Mage("Mage")
    paladin = Paladin("Paladin")


    inventory_warrior = Inventory(warrior)
    inventory_mage = Inventory(mage)
    inventory_paladin = Inventory(paladin)


    clothing = Clothing("Leather Armor")
    weapon = Weapon("Sword")
    artifact = Artifact("Amulet")


    inventory_warrior.add_item(clothing)
    inventory_warrior.add_item(weapon)

    inventory_mage.add_item(clothing)
    inventory_mage.add_item(artifact)

    inventory_paladin.add_item(weapon)
    inventory_paladin.add_item(artifact)


    print("Warrior's Inventory:", [item.name for item in inventory_warrior.get_inventory()])
    print("Mage's Inventory:", [item.name for item in inventory_mage.get_inventory()])
    print("Paladin's Inventory:", [item.name for item in inventory_paladin.get_inventory()])