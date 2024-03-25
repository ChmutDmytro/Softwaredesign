class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def create_hero(self):
        self.builder.set_height("Tall") \
                    .set_build("Athletic") \
                    .set_hair_color("Blonde") \
                    .set_eye_color("Blue") \
                    .set_clothing("Armor") \
                    .set_inventory("Sword") \
                    .set_good_deeds(["Saving the kingdom", "Helping the needy"])
        return self.builder.get_character()

    def create_enemy(self):
        self.builder.set_height("Average") \
                    .set_build("Stocky") \
                    .set_hair_color("Black") \
                    .set_eye_color("Red") \
                    .set_clothing("Robes") \
                    .set_inventory("Magic Staff") \
                    .set_evil_deeds(["Conquering kingdoms", "Summoning dark creatures"])
        return self.builder.get_character()

class HeroBuilder:
    def __init__(self):
        self.character = Character()

    def set_height(self, height):
        self.character.height = height
        return self

    def set_build(self, build):
        self.character.build = build
        return self

    def set_hair_color(self, hair_color):
        self.character.hair_color = hair_color
        return self

    def set_eye_color(self, eye_color):
        self.character.eye_color = eye_color
        return self

    def set_clothing(self, clothing):
        self.character.clothing = clothing
        return self

    def set_inventory(self, inventory):
        self.character.inventory = inventory
        return self

    def set_good_deeds(self, good_deeds):
        self.character.good_deeds = good_deeds
        return self

    def get_character(self):
        return self.character

class EnemyBuilder:
    def __init__(self):
        self.character = Character()

    def set_height(self, height):
        self.character.height = height
        return self

    def set_build(self, build):
        self.character.build = build
        return self

    def set_hair_color(self, hair_color):
        self.character.hair_color = hair_color
        return self

    def set_eye_color(self, eye_color):
        self.character.eye_color = eye_color
        return self

    def set_clothing(self, clothing):
        self.character.clothing = clothing
        return self

    def set_inventory(self, inventory):
        self.character.inventory = inventory
        return self

    def set_evil_deeds(self, evil_deeds):
        self.character.evil_deeds = evil_deeds
        return self

    def get_character(self):
        return self.character

class Character:
    def __init__(self):
        self.height = None
        self.build = None
        self.hair_color = None
        self.eye_color = None
        self.clothing = None
        self.inventory = None
        self.evil_deeds = []
        self.good_deeds = []

    def __str__(self):
        return f"Character: Height: {self.height}, Build: {self.build}, Hair Color: {self.hair_color}, Eye Color: {self.eye_color}, Clothing: {self.clothing}, Inventory: {self.inventory}, Evil Deeds: {self.evil_deeds}, Good Deeds: {self.good_deeds}"

def main():
    director = Director()
    hero_builder = HeroBuilder()
    director.set_builder(hero_builder)

    hero = director.create_hero()
    print("Hero:")
    print(hero)

    enemy_builder = EnemyBuilder()
    director.set_builder(enemy_builder)

    enemy = director.create_enemy()
    print("\nEnemy:")
    print(enemy)

if __name__ == "__main__":
    main()