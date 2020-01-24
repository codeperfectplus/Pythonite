# Over Loading Method

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x 
        self.y += y

    def __add__(self, other):
        return Point(self.x + other.x, self.y+other.y)
    
    def __sub__(self,other):
        return Point(self.x - other.x, self.y- other.y)
    
    def __mul__(self,other):
        return self.x * other.x , self.y * other.y

p1 = Point(3,4)
p2 = Point(3,2)

p3 = p1+ p2 
p4 = p1-p2
p7 =p1*p2 