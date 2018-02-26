    #distance formula
   #under root(x2-x1) **2 + (y2-y1) **2
   #slope formula
   #y2-y1/x2-x1
import math
class Line(object):

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        c = math.sqrt((x2-x1) ** 2 +(y2-y1) ** 2)
        return c

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        v = (float(y2)-float(y1))/(float(x2)-float(x1))
        return v

coor1 = (3, 2)
coor2 = (8,10)
print(Line(coor1,coor2).slope())
print(Line(coor1,coor2).distance())
