class Vec2D():
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)