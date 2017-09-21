import sys
import datetime
import pygame as pg
from lockedBody import LockedBody
from circularPath import CircularPath
from time import sleep

class Game():
    """ A class to run the game loop, handle window size and
        calculate time between update steps """

    def __init__(self, width=320, height=240, minDt=5):
        """ Initialises the screen size and minimum step delay(milliseconds) """
        pg.init()
        self.width    = width
        self.height   = height
        self.minDt    = minDt
        self.gameOver = False
        self.screen   = pg.display.set_mode((self.width, self.height), 
                        pg.HWSURFACE|pg.DOUBLEBUF|pg.RESIZABLE)
        self.setupSystem()           
    
    def setupSystem(self):
        self.lockedBodies = [
            LockedBody(radius=20, color=pg.Color(255,255,0,255)),
            LockedBody(position=(100,0), radius=10, color=pg.Color(0,0,255,255), speed=-1),
            LockedBody(position=(20,20), radius=5, color=pg.Color(255,255,255,255) ,speed=-3)
        ]
        
        # Set parent of moon to earth
        self.lockedBodies[2].setParent(self.lockedBodies[1])
        self.lockedBodies[2].setPath(CircularPath())
        
        # Set earth parent to moon
        self.lockedBodies[1].setParent(self.lockedBodies[0])
        self.lockedBodies[1].setPath(CircularPath())
    
    def worldToScreen(self, pos):
        """ Converts a world position to a screen position, requires tuple for x and y """
        return (int(pos[0]) + self.width/2, int(pos[1]) + self.height/2)  
    
    def step(self, dt):
        """ Computes one game step or tick, dt being the 
            approx time elapsed since the previous tick """
            
        black = (0, 0, 0)
        self.screen.fill(black)
        for body in self.lockedBodies:
            body.update(dt)
            body.draw(self.screen, self.worldToScreen(body.getWorldPosition()))
        
        pg.display.flip()
    
    def gameLoop(self):
        """ Loops until gameOver is set to true. A minimum time between updates
            is enforced, and elapsed time is calculated to an approximate value. """
            
        taken = self.minDt
        while not self.gameOver:
            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()
                elif event.type==pg.VIDEORESIZE: self.screenResize(event)            
            start = datetime.datetime.now()
            self.step(taken)
            taken = datetime.datetime.now() - start
            taken = taken.total_seconds() * 1000
            if taken < self.minDt:
                sleep((self.minDt - taken)/1000)
                taken = self.minDt
    
    def screenResize(self, data):
        self.width, self.height = data.dict["size"]
        self.screen = pg.display.set_mode((self.width, self.height), 
                      pg.HWSURFACE|pg.DOUBLEBUF|pg.RESIZABLE)  