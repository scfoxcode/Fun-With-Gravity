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
            LockedBody(radius=25, color=pg.Color(255,255,0,255)),
            LockedBody(position=(150,0), radius=10, color=pg.Color(0,0,255,255), speed=-1),
            LockedBody(position=(14,14), radius=5, color=pg.Color(255,255,255,255) ,speed=-3),
            LockedBody(position=(24,-24), radius=2, color=pg.Color(180,180,240,255) ,speed=-2),
            LockedBody(position=(-60, 0), radius=6, color=pg.Color(255,128,0,255) ,speed=-3),
            LockedBody(position=(220, 220), radius=18, color=pg.Color(255,70,20,255) ,speed=-0.3),
            LockedBody(position=(40, 40), radius=5, color=pg.Color(50,255,100,255) ,speed=-1),
            LockedBody(position=(55,-55), radius=4, color=pg.Color(200,40,255,255) ,speed=-0.8),
            LockedBody(position=(30,0), radius=7, color=pg.Color(200,200,255,255) ,speed=-3)
        ]
        
        # Set parent of moon 1 to habitable
        self.lockedBodies[2].setParent(self.lockedBodies[1])
        self.lockedBodies[2].setPath(CircularPath())
        
        # Set parent of moon 2 to habitable
        self.lockedBodies[3].setParent(self.lockedBodies[1])
        self.lockedBodies[3].setPath(CircularPath())
        
        # Set habitable parent to sun
        self.lockedBodies[1].setParent(self.lockedBodies[0])
        self.lockedBodies[1].setPath(CircularPath())
        
        # Set inner parent to sun
        self.lockedBodies[4].setParent(self.lockedBodies[0])
        self.lockedBodies[4].setPath(CircularPath())
        
        # Set gas giant parent to sun
        self.lockedBodies[5].setParent(self.lockedBodies[0])
        self.lockedBodies[5].setPath(CircularPath())
        
        # Set moon 3 parent to gas giant
        self.lockedBodies[6].setParent(self.lockedBodies[5])
        self.lockedBodies[6].setPath(CircularPath())
        
        # Set moon 4 parent to gas giant
        self.lockedBodies[7].setParent(self.lockedBodies[5])
        self.lockedBodies[7].setPath(CircularPath())
        
        # Set moon 5 parent to gas giant
        self.lockedBodies[8].setParent(self.lockedBodies[5])
        self.lockedBodies[8].setPath(CircularPath())
    
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