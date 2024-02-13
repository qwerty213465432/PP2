import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, nn_point):
        distance = math.sqrt((self.x - nn_point.x)**2 + (self.y - nn_point.y)**2) 
        return distance


a=int(input())
b=int(input())
c=int(input())
d=int(input())
point1 = Point(a, b)
point2 = Point(c, d)
point1.show()
point2.show()

distance = point1.dist(point2)
print( distance)
