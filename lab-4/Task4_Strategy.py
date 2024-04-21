from abc import ABC, abstractmethod

# Інтерфейс стратегії
class ImageLoadingStrategy(ABC):
    @abstractmethod
    def load_image(self, href):
        pass

# Конкретна стратегія для завантаження картинки з файлової системи
class FilesystemImageLoadingStrategy(ImageLoadingStrategy):
    def load_image(self, href):
        # Реалізація завантаження з файлової системи
        return f"Image loaded from filesystem: {href}"

# Конкретна стратегія для завантаження картинки з мережі
class NetworkImageLoadingStrategy(ImageLoadingStrategy):
    def load_image(self, href):
        # Реалізація завантаження з мережі
        return f"Image loaded from network: {href}"

# Клас Image, який використовує стратегію
class Image:
    def __init__(self, href, loading_strategy):
        self.href = href
        self.loading_strategy = loading_strategy

    def display(self):
        image_data = self.loading_strategy.load_image(self.href)
        print(image_data)

if __name__ == "__main__":
    # Використання класу Image з конкретними стратегіями
    image_from_filesystem = Image("path/to/image.jpg", FilesystemImageLoadingStrategy())
    image_from_network = Image("http://example.com/image.jpg", NetworkImageLoadingStrategy())

    # Відображення картинок
    image_from_filesystem.display()
    image_from_network.display()