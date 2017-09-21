import math

class Vec2D():
    """ Defines a simple 2D vector class, limitted functionality, 
    functions were added as needed """
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
        return vec.x**2 + vec.y**2
    
    @staticmethod
    def magnitude(vec):
        value = Vec2D.magnitudeSquared(vec)
        return math.sqrt(value)
    
    @staticmethod
    def scale(vec, value):
        return Vec2D(vec.x*value, vec.y*value)
        
    @staticmethod
    def normalize(vec):
        size = max(1, Vec2D.magnitude(vec))
        return  Vec2D.scale(vec, 1.0/size)
        
    
        
        