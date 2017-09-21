import math

class Vec2D():
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)
        
    @staticmethod
    def rotate(vec, theta):
        sn = math.sin(theta)
        cs = math.cos(theta)
        x = vec.x * cs - vec.y * sn
        y = vec.x * sn + vec.y * cs
        return Vec2D(x, y)
    
    @staticmethod
    def magnitudeSquared(vec):
        return Vec2D(x**x, y**y)
    
    @staticmethod
    def magnitude(vec):
        value = Vec2D.magnitudeSquared(vec)
        return math.sqrt(value)
        