import pygame as pg

class UserInput():
    
    def __init__(self):
        self.leftMouse   = False
        self.middleMouse = False
        self.rightMouse  = False
    
    def update(self):
        left, middle, right = pg.mouse.get_pressed()
        
        if left and not self.leftMouse: # On mouse down
            print("mouseDown")
        elif not left and self.leftMouse: # On mouse Up
            print("mouseUp")
        
        self.leftMouse, self.middleMouse, self.rightMouse = (left, middle, right)