import pygame as pg

class Drawable(object):

    def __init__(self, color=pg.Color(255,255,255,255), radius=10):
        self.color  = color
        self.radius = radius
    
    def draw(self, surface, pos):
        pg.draw.circle(surface, pg.Color(255,255,0,255), 
                       (pos[0]/2, pos[1]/2), self.radius)
    
    