import math

class Shape:
    def __init__(self, name):
        self.name = name  

    def area(self):
        return 0

    def perimeter(self):
        return 0

    def __str__(self):
        return f"Shape: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.__radius = radius  

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return f"{self.name} with radius {self.__radius}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.__width = width     
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"{self.name} of width {self.__width} and height {self.__height}"


def print_shape_info(shape):
    print(shape)  
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
    print("Repr:", repr(shape))
    print("---")


    def __init__(self, shapes):
        self.shapes = shapes

    def __add__(self, other):
        return ShapeGroup(self.shapes + other.shapes)

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

    def total_perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)

    def __str__(self):
        return f"ShapeGroup with {len(self.shapes)} shapes"


circle = Circle(5)
rectangle = Rectangle(4, 6)

print_shape_info(circle)
print_shape_info(rectangle)

group1 = ShapeGroup([circle])
group2 = ShapeGroup([rectangle])
combined = group1 + group2  

print(combined)
print("Combined Area:", combined.total_area())
print("Combined Perimeter:", combined.total_perimeter())
