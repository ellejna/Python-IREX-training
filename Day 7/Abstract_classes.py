from abc import ABC, abstractmethod # import Abstract Base Class

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
    def perimeter(self):
        return 4 * self.length

square = Rectangle(5)
print("The squares area is", square.area())
print("The squares perimeter is", square.perimeter())
