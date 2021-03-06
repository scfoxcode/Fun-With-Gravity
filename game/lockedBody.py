import pygame as pg
from vec2D import Vec2D
from dynamicBody import DynamicBody

class LockedBody():
    """ A locked body is used to represent a stationary object
        or one that follows a well defined path. It may have
        mass and therefore gravity, but is not affected
        by any forces """
    
    def __init__(self, position=Vec2D(0,0), mass=1.0, speed=1, radius=10, color=pg.Color(255,255,255,255), parent=None):
        self.position   = position # Position is relative to parent if a parent exists
        self.speed      = speed
        self.mass       = mass
        self.radius     = radius
        self.color      = color
        self.parentBody = parent
        self.path       = None
        self.children   = []
    
    def __iter__(self):
        """ Used to iterate over this node and all it's children """
        for child in self.children:
            for leaf in child:
                yield leaf
        yield self
    
    def update(self, dt):
        """ Updates the position using the path """
        if self.path:
            self.position = self.path.updatePosition(self.position, self.speed, dt)
        
    def setPath(self, path):
        """ Sets the path to follow """
        self.path = path
    
    def setParent(self, parentBody):
        """ Hold a reference to a parent body. Our position and movement
            is now relative to the parent """
        self.parentBody = parentBody
    
    def addChild(self, child):
        """ Adds a child node. The child's movements will be relative to this node's position """
        if child:
            self.children.append(child)

    def getWorldPosition(self):
        """ Converts our local position into world space by calling the parents world position """
        position = self.position
        if self.parentBody:
            position = self.parentBody.getWorldPosition()
        return position + self.position
        