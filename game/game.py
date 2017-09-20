import sys
import datetime
import pygame as pg
from lockedBody import LockedBody
from time import sleep

class Game():
    """ A class to run the game loop, handle window size and
        calculate time between update steps """

    def __init__(self, width=320, height=240, minDt=5):
        """ Initialises the screen size and minimum step delay(milliseconds)"""
        pg.init()
        self.width    = width
        self.height   = height
        self.minDt    = minDt
        self.gameOver = False
        self.screen   = pg.display.set_mode((self.width, self.height), 
                        pg.HWSURFACE|pg.DOUBLEBUF|pg.RESIZABLE)
        self.lockedBodies = []
        self.lockedBodies.append(LockedBody())
    
    def worldToScreen(self, pos):
        return (pos[0] + self.width, pos[1] + self.height)
        
    
    def step(self, dt):
        """ Computes one game step or tick, dt being the 
            approx time elapsed since the previous tick """
            
        black = (0, 0, 0)
        self.screen.fill(black)
        # Render bodies
        for body in self.lockedBodies:
            body.draw(self.screen, self.worldToScreen(body.position))
        
        pg.display.flip()
    
    def gameLoop(self):
        """ Loops until gameOver is set to true. A minimum time between updates
            is enforced, and elapsed time is calculated to an approximate value. """
            
        taken = self.minDt
        while not self.gameOver:
            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()
            start = datetime.datetime.now()
            self.step(taken)
            taken = datetime.datetime.now() - start
            taken = taken.total_seconds() * 1000
            if taken < self.minDt:
                sleep((self.minDt - taken)/1000)
                taken = self.minDt