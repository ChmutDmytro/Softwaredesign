from zoo_classes import Animal, Enclosure, ZooKeeper, ZooManager, Inventory, MonthlyStatistics

def main():

    lion = Animal("Leo", "Lion")
    tiger = Animal("Tina", "Tiger")


    big_enclosure = Enclosure(size="Large", enclosure_type="Jungle")
    big_enclosure.add_animal(lion)
    big_enclosure.add_animal(tiger)


    zookeeper = ZooKeeper(name="John", role="Zoo Keeper")


    zoo_inventory = Inventory()
    monthly_statistics = MonthlyStatistics()


    print("\n=== Інформація про тварин в вольєрі ===")
    zoo_inventory.display_animals(big_enclosure)


    print("\n=== Інформація про працівника зоопарку ===")
    zoo_inventory.display_employees([zookeeper])


    print("\n=== Годування тварини ===")
    lion.feed("meat")
    monthly_statistics.record_feeding()


    print("\n=== Процес годування тварини зоокіпером ===")
    zookeeper.feed_animal(tiger, "fish")
    monthly_statistics.record_keeper_interaction()


    print("\n=== Місячна статистика ===")
    monthly_statistics.display_statistics()

    if __name__ == "__main__":
         main()