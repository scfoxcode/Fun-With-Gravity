from drawable import Drawable
import pygame as pg

class LockedBody(Drawable):
    """ A locked body is used to represent a stationary object
        or one that follows a well defined path. It may have
        mass and therfore gravity, but is not affected
        by any forces"""
    
    def __init__(self, position=(0,0), mass=1.0, radius=10, color=pg.Color(255,255,255,255)):
        self.position   = position # This is local to parent if a parent exists
        self.mass       = mass
        self.radius     = radius
        self.color      = color
        self.path       = None
        self.parentBody = None
        super(LockedBody, self).__init__(radius=self.radius, color=self.color)
    
    def update(self, dt):
        if self.path == None:
            return
    
    def setParent(self, parentBody):
        """ Hold a reference to a parent body. Our position and movement
            is now relative to the parent """
 
        self.parentBody = parentBody

    def getWorldPosition(self):
        position = self.position
        if self.parentBody:
            position = self.parentBody.getWorldPosition()
            position = (position[0] + self.position[0],
                        position[1] + self.position[1])
        return position
        