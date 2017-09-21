import pygame as pg
from dynamicBody import DynamicBody
from vec2D import Vec2D

class UserInput():
    
    def __init__(self):
        self.body          = None
        self.clickPosition = None
        self.gameRef       = None
        self.leftMouse     = False
        self.middleMouse   = False
        self.rightMouse    = False
    
    def createDynamicBody(self, position):
        self.body = DynamicBody(position=position)
        
    def updateDynamicPosition(self, position):
        self.body.position = position
    
    def update(self):
        x, y = pg.mouse.get_pos()
        mousePos = Vec2D(x, y)
        left, middle, right = pg.mouse.get_pressed()
        
        if left and not self.leftMouse:   # On mouse down
            self.clickPosition = mousePos
            self.createDynamicBody(mousePos)
        elif not left and self.leftMouse: # On mouse Up
            print("temp")

        if self.leftMouse:
            self.updateDynamicPosition(mousePos)
        
        self.leftMouse, self.middleMouse, self.rightMouse = (left, middle, right)