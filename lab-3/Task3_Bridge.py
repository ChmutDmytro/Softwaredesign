# Базовий клас для фігур
class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        raise NotImplementedError("Method 'draw' must be implemented in subclass")

# Класи для рендерерів
class Renderer:
    def render(self, shape):
        raise NotImplementedError("Method 'render' must be implemented in subclass")

class VectorRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape.name} as vector graphic")

class RasterRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape.name} as pixels")

# Класи для фігур
class Circle(Shape):
    def __init__(self, name, radius, renderer):
        super().__init__(name)
        self.radius = radius
        self.renderer = renderer

    def draw(self):
        self.renderer.render(self)

class Square(Shape):
    def __init__(self, name, side_length, renderer):
        super().__init__(name)
        self.side_length = side_length
        self.renderer = renderer

    def draw(self):
        self.renderer.render(self)

class Triangle(Shape):
    def __init__(self, name, base, height, renderer):
        super().__init__(name)
        self.base = base
        self.height = height
        self.renderer = renderer

    def draw(self):
        self.renderer.render(self)


if __name__ == "__main__":

    # Створення рендерерів
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    # Створення фігур
    circle = Circle("Circle", 5, vector_renderer)
    square = Square("Square", 4, raster_renderer)
    triangle = Triangle("Triangle", 3, 6, vector_renderer)

    # Виклик методу draw для кожної фігури
    circle.draw()
    square.draw()
    triangle.draw()