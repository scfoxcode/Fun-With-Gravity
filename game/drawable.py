import pygame as pg

class Drawable(object):

    def __init__(self, color=pg.Color(255,255,255,255), radius=10):
        self.color  = color
        self.radius = radius
    
    def draw(self, surface, pos):
        pg.draw.circle(surface, self.color, 
                      (pos[0], pos[1]), self.radius)
    
    