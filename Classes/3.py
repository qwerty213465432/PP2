<<<<<<< HEAD
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


x=int(input())
y=int(input())
rectangle = Rectangle(x, y)
print(rectangle.area())
=======
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


x=int(input())
y=int(input())
rectangle = Rectangle(x, y)
print(rectangle.area())
>>>>>>> 4f5a363e377dab23b995e5eeecba25a7e240298a
