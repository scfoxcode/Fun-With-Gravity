import sys
import datetime
import pygame as pg
from time import sleep

class Game():
    """ A class to run the game loop, handle window size and
        calculate time between update steps """

    def __init__(self, width=640, height=480, minDt=5):
        """ Initialises the screen size and minimum step delay(milliseconds)"""
        
        self.width    = width
        self.height   = height
        self.minDt    = minDt
        self.gameOver = False
        self.screen   = pg.display.set_mode((self.width, self.height), 
                        pg.HWSURFACE|pg.DOUBLEBUF|pg.RESIZABLE)
    
    def step(self, dt):
        """ Computes one game step or tick, dt being the 
            approx time elapsed since the previous tick """
            
        black = (0, 0, 0)
        self.screen.fill(black)
        pg.draw.circle(self.screen, pg.Color(255,255,0,255), (self.width/2, self.height/2), 20)
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