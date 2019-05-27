import turtle 

t = turtle.Turtle()

#UDT - Point
class Point :
    #Constructor
    def __init__(self, x, y) :
        self.X = x
        self.Y = y
    #Member Function
    def getX(self) :
        return self.X
    def getY(self) :
        return self.Y
    def getPoint(self) :
        return Point(self.X,self.Y)

#UDT - Line
class Line:
    #Constructor
    def __init__(self,p1,p2):
        self.Draw(p1,p2)
    #Member Function
    def Draw(self,p1,p2) :
        t.penup()
        t.goto(p1.getX(),p1.getY())
        t.pendown()
        t.goto(p2.getX(),p2.getY())
        
#UDT - Circle
class Circle :
    #Constructor
    def __init__(self, r, c):
        self.radius = r
        self.center = Point(c.getX(),c.getY())
    #Member Function
    def Draw(self):
        t.penup()
        t.goto(self.center.getX(),self.center.getY()/2)
        t.pendown()
        t.circle(self.radius)

#UDT - Triangle
class Triangle :
    #Constructor
    def __init__(self,t,l,r):
        self.top = Point(t.getX(),t.getY())
        self.left = Point(l.getX(),l.getY())
        self.right = Point(r.getX(),r.getY())
    #Member Function
    def Draw(self):
        line = Line(self.top,self.left)
        line.Draw(self.left,self.right)
        line.Draw(self.right,self.top)

#UDT - Rectangle
class Rectangle:
    #Constructor
    def __init__(self,p,h,w):
        self.topleft = Point(p.getX(),p.getY())
        self.height = h
        self.width = w
    #Member Function
    def Draw(self):
        x = self.topleft.getX()
        y = self.topleft.getY()
        h = self.height
        w = self.width
        line = Line(self.topleft,Point(x,y+h))
        line.Draw(Point(x,y+h),Point(x+w,y+h))
        line.Draw(Point(x+w,y+h),Point(x+w,y-h))
        line.Draw(Point(x+w,y-h),Point(x,y-h))
        line.Draw(Point(x,y-h),self.topleft)

class Geometry :
    def __init__(self):
        pass
    def Circle(self,radius,center):
        c = Circle(radius,center)
        c.Draw()
    def Triangle(self,top,left,right):
        t = Triangle(top,left,right)
        t.Draw()
    def Rectangle(self,top,height,width):
        r = Rectangle(top,height,width)
        r.Draw()
        
#geometry object
g = Geometry()

#point object
p = Point(100,50)
print(p.getX())
print(p.getY())
q = p.getPoint()
print(q.getX())
print(q.getY())

#circle
p.X = 0
p.Y = 100
g.Circle(100,p)

#triangle
top = Point(0,100)
left = Point(-100,-100)
right = Point(100,-100)
g.Triangle(top,left,right)

#rectangle
g.Rectangle(top,100,200)


