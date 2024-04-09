import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


point1 = Point(3, 4)
point2 = Point(6, 8)

print("Coordinates of point1:", point1.get_coordinates())
print("Coordinates of point2:", point2.get_coordinates())

distance = point1.distance_to(point2)
print("Distance between point1 and point2:", distance)

point1.set_coordinates(1, 2)
print("New coordinates of point1:", point1.get_coordinates())
