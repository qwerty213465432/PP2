<<<<<<< HEAD
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2



shape = Shape()
print(shape.area())

x=int(input())
square = Square(x)
print( square.area())
=======
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2



shape = Shape()
print(shape.area())

x=int(input())
square = Square(x)
print( square.area())
>>>>>>> 4f5a363e377dab23b995e5eeecba25a7e240298a
