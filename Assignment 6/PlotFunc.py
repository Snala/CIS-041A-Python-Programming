import turtle 

t = turtle.Turtle() 

class PointList:
    def __init__(self,plist):
        self.points = plist
    def minX(self):
        min = self.points[0][0]
        for x in range(1,len(self.points)):
            if self.points[x][0] < min:
                min = self.points[x][0]
        return min
    def minY(self):
        min = self.points[0][1]
        for y in range(1,len(self.points)):
            if self.points[y][1] < min:
                min = self.points[y][1]
        return min  
    def maxX(self):
        max = self.points[0][0]
        for x in range(1,len(self.points)):
            if self.points[x][0] > max:
                min = self.points[x][0]
        return min
    def maxY(self):
        max = self.points[0][1]
        for y in range(1,len(self.points)):
            if self.points[y][1] > max:
                min = self.points[y][1]
        return min      
    
def Plot():
    t = turtle.Turtle() 
    screen = turtle.Screen()
    points = [[0,0],[1,1],[2,0],[3,-1],[4,0]]   
    plist = PointList(points)
    screen.setworldcoordinates( plist.minX(),plist.minY(),plist.maxX(),plist.maxY() )
    for p in range(len(points)-1):
        t.up()
        t.goto(points[p][0],points[p][1])
        t.down()
        t.goto(points[p+1][0],points[p+1][1])
    turtle.exitonclick()
    
Plot()