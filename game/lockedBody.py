from drawable import Drawable

class LockedBody(Drawable):
    """ A locked body is used to represent a stationary object
        or one that follows a well defined path. It may have
        mass and therfore gravity, but is not affected
        by any forces"""
    
    def __init__(self, position=(0,0), mass=1.0, radius=10):
        self.position = position
        self.mass     = mass
        self.radius   = radius
        self.path     = None
        super(LockedBody, self).__init__()
    
    def update(self, dt):
        if self.path == None:
            return