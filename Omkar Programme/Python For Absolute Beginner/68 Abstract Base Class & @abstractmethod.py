from abc import ABC, abstractmethod   # import module

class Shape(ABC):     # Parents class Shape
    @abstractmethod      # restriction to make function to every child class
    def printarea(self):
        return 0

class Rectangle(Shape):   # child class of Shape
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 9
        self.breath = 4

    def printarea(self):        # restricted function from parent class
        return self.length * self.breath

rect1 = Rectangle()
print(rect1.printarea())
rect2 = Shape()         # cannot make objects using abstract class