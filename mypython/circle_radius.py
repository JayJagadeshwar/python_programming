class Circle(object):
    pi = 3.1415
    def __init__(self, radius = 1):
        self.radius = radius
    def area(self):
        return (self.radius**2) * Circle.pi

c = Circle(radius= 100)
print(c.area())
print(Circle().radius)
