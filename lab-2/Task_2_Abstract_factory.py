from abc import ABC, abstractmethod

# Абстрактний клас пристрою
class Device(ABC):
    @abstractmethod
    def create(self):
        pass

# Класи різних пристроїв
class Laptop(Device):
    def create(self):
        return "Laptop"

class Netbook(Device):
    def create(self):
        return "Netbook"

class EBook(Device):
    def create(self):
        return "EBook"

class Smartphone(Device):
    def create(self):
        return "Smartphone"

# Абстрактна фабрика
class TechFactory(ABC):
    @abstractmethod
    def produce_laptop(self):
        pass

    @abstractmethod
    def produce_netbook(self):
        pass

    @abstractmethod
    def produce_ebook(self):
        pass

    @abstractmethod
    def produce_smartphone(self):
        pass

# Фабрики для різних брендів
class IProneFactory(TechFactory):
    def produce_laptop(self):
        return Laptop()

    def produce_netbook(self):
        return Netbook()

    def produce_ebook(self):
        return EBook()

    def produce_smartphone(self):
        return Smartphone()

class XiaomiFactory(TechFactory):
    def produce_laptop(self):
        return Laptop()

    def produce_netbook(self):
        return Netbook()

    def produce_ebook(self):
        return EBook()

    def produce_smartphone(self):
        return Smartphone()

class GalaxyFactory(TechFactory):
    def produce_laptop(self):
        return Laptop()

    def produce_netbook(self):
        return Netbook()

    def produce_ebook(self):
        return EBook()

    def produce_smartphone(self):
        return Smartphone()

# Використання фабрики
def main():
    iprone_factory = IProneFactory()
    xiaomi_factory = XiaomiFactory()
    galaxy_factory = GalaxyFactory()

    devices = [
        iprone_factory.produce_laptop(),
        iprone_factory.produce_netbook(),
        iprone_factory.produce_ebook(),
        iprone_factory.produce_smartphone(),
        xiaomi_factory.produce_laptop(),
        xiaomi_factory.produce_netbook(),
        xiaomi_factory.produce_ebook(),
        xiaomi_factory.produce_smartphone(),
        galaxy_factory.produce_laptop(),
        galaxy_factory.produce_netbook(),
        galaxy_factory.produce_ebook(),
        galaxy_factory.produce_smartphone()
    ]

    for device in devices:
        print(device.create())

if __name__ == "__main__":
    main()