import math
class Shape():

    def Shape():
       pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return  math.pi * ((self.radius)**2) 



class Rectangle(Shape):
    def __init__(self,lenght ,width):
        self.length = lenght
        self.width = width

    def Area(self):
        return  self.length * self.width


class Triangle(Shape):
    def __init__(self,base , height):
        self.base = base
        self.height = height

    def Area(self):
        return 0.5 * (self.base * self.height)


C = Circle(25)
print(C.Area()) 
         
R = Rectangle(12 ,15)
print(R.Area())
# C.Area

T = Triangle(5 , 10)
print(T.Area())