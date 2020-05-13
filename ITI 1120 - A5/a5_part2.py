class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    'class that represent a rectangle on the plane'
    def __init__(self, bottom=Point(0,0), top=Point(0,0), colour="'None'"):
        '''(Point,Point, str) -> None
        initialize rectangle with bottom left corner, top right corner, and bottom corner
        '''
        self.bot = bottom
        self.top = top
        self.colour = str(colour)

    def get_color(self):
        '''None -> str
        returns colour of rectangle
        '''
        return self.colour
    
    def get_bottom_left(self):
        '''None-> Point
        returns coordinates of bottom left corner
        '''
        return self.bot
    def get_top_right(self):
        '''None -> Point
        returns coordinates of top right corner
        '''
        return self.top
    def reset_color(self, colour):
        '''changes colour of rectangle to that specified
        '''
        self.colour = colour

    def get_perimeter(self):
        '''(Rectangle)-> num
        returns the perimeter of the rectangle
        '''
        x = self.top.x - self.bot.x
        y = self.top.y - self.bot.y
        return 2*y+2*x
    def get_area(self):
        ''' (Rectangle) -> num
        returns area of rectangle
        '''
        x = self.top.x - self.bot.x
        y = self.top.y - self.bot.y
        return x*y
    
    def move(self, dx, dy):
        '''(num,num) -> Rectangle
            moves rectangle along x and y axis according to spec
        '''
        self.bot.move(dx,dy)
        self.top.move(dx,dy)

    def contains(self, pointx, pointy):
        ''' (Rectangle, Point) -> bool
        determines if a point is located inside of rectangle
        '''
        x = self.bot.x<=pointx<=self.top.x
        y = self.bot.y<=pointy<=self.top.y
        return x and y
        
        
    def intersects(self, other):
        ''' (Rectangle, Rectangle) -> bool
        determines if 2 rectangles intersect on plane
        '''
        # rectangle 1
        r1y1 = self.bot.y   #bottom
        r1y2 = self.top.y   #top
        r1x1 = self.bot.x   #left
        r1x2 = self.top.x   #right

        # rectangle 2
        r2y1 = other.bot.y  #bottom
        r2y2 = other.top.y  #top
        r2x1 = other.bot.x  #left
        r2x2 = other.top.x  #right

        # corners a point in rectangle
        r1inr2corner = self.contains(r2x1,r2y1) or self.contains(r2x1,r2y2) or self.contains(r2x2,r2y1) or self.contains(r2x2,r2y2)
        r2inr1corner = other.contains(r1x1,r1y1) or other.contains(r1x1,r1y2) or other.contains(r1x2,r1y1) or other.contains(r1x2,r1y2)

        # no corners inside, overlapping
        crossiny = r2y1<r1y1<=r2y2 and r2y1<r1y2<=r2y2 and r1x1<r2x1<r1x2 and r1x1<r2x2<r1x2
        crossinyr2 = r1y1<r2y1<=r1y2 and r1y1<r2y2<=r1y2 and r2x1<r1x1<r2x2 and r2x1<r1x2<r2x2

        crossinx = r2x1<r1x1<=r2x2 and r2x1<r1x2<=r2x2 and r1y1<r2y1<r1y2 and r1y1<r2y2<r1y2
        crossinxr2 = r1x1<r2x1<=r1x2 and r1x1<r2x2<=r1x2 and r2y1<r1y1<r2y2 and r2y1<r1y2<r2y2   

        return r1inr2corner or r2inr1corner or crossiny or crossinyr2 or crossinx or crossinxr2

    def __eq__(self, other):
        '''(Rectangle, Rectangle)->bool
        returns whether values of rectangle are equal
        '''
        return self.bot == other.bot and self.top == other.top and self.colour == other.colour
    
    def __repr__(self):
        '''(Rectangle)->str
        return canonical string representation of object Rectangle(bottom,top,colour)
        '''
        return ("Rectangle(" + str(self.bot) + ", " + str(self.top) + ", '" + str(self.colour) + "')")
    def __str__(self):
        '''(Rectangle)-> str
        returns nice string representation of rectangle(bot, top, colour)
        '''
        return (" I am a " + str(self.colour) + " rectangle with bottom left corner at " + str(self.bot) + " and top right corner at " + str(self.top) + ".")


class Canvas:
    ''' a collection of rectangles
    '''
    def __init__(self, rectangles = []):
        '''(none)->list
        initialize list to hold rectangles
        '''
        self.rectangles = []

    def add_one_rectangle(self, rect = Rectangle()):
        '''(Rectangle)-> num
        adds a rectangle to the canvas
        '''
        self.rectangles.append(rect)

    def count_same_color(self, colour):
        '''(str)-> num
        counts number of rectangles on canvas with specified colour
        '''
        count = 0
        for i in self.rectangles:
            if i.colour == colour:
                count+=1
        return count
    
    def total_perimeter(self):
        '''none->num
        sum perimeter of all rectangles on the canvas
        '''
        total = 0
        for i in self.rectangles:
            total += i.get_perimeter()
        return total

    def min_enclosing_rectangle(self): # understand this thing
        '''none->Rectangle
        returns the min enclosing rectangle of the canvas
        '''
        boty = self.rectangles[0].bot.y
        botx = self.rectangles[0].bot.x
        topy = self.rectangles[0].top.y
        topx = self.rectangles[0].top.x

        for i in self.rectangles:
            if i.top.y > topy:
                topy = i.top.y
            if i.top.x > topx:
                topx = i.top.x
            if i.bot.y < boty:
                boty = i.bot.y
            if i.bot.x < botx:
                botx = i.bot.x
        return Rectangle(Point(botx,boty),Point(topx,topy))

    def common_point(self):
        '''none -> Bool
        returns true/false depending if there is a point common to all rectangles
        ''' 
        i = 0
        state = True
        while state == True and i<=len(self.rectangles)-2:
            state = self.rectangles[i].intersects(self.rectangles[i+1])
            i+=1
        return state
            
    
    def __repr__(self):
        '''none->str
        Returns canonical string representation Canvas'''
        return 'Canvas('+str(self.rectangles)+')'

    def __len__(self):
        '''none ->str
        returns number of rectangles on canvas
        '''
        length = 0
        for i in self.rectangles:
            length+=1
        return length
    
            
    

    
                
