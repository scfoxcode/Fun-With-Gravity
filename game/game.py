import sys
import pygame as pg
from userInput import UserInput
from lockedBody import LockedBody
from circularPath import CircularPath
from time import sleep, clock

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
        pg.display.set_caption("Fun-With-Gravity")
        self.input = UserInput()
        self.setupSystem()   
    
    def setupSystem(self):        
        # Create the sun
        self.rootBody  = LockedBody(radius=35, color=pg.Color(255,255,0,255))
        
        # Create planets
        innerPlanet    = LockedBody(position=(-70, 0)  , radius=6 , color=pg.Color(255,128,0,255) ,speed=-3)
        middlePlanet   = LockedBody(position=(150,0)   , radius=10, color=pg.Color(0,0,255,255)   , speed=-1)
        outerPlanet    = LockedBody(position=(220, 220), radius=18, color=pg.Color(255,70,20,255) ,speed=-0.3)
        self.rootBody.addChild(innerPlanet)
        self.rootBody.addChild(middlePlanet)
        self.rootBody.addChild(outerPlanet)
        
        # Add moons
        middlePlanet.addChild(LockedBody(position=(14,14) , radius=5, color=pg.Color(255,255,255,255) ,speed=-3))
        middlePlanet.addChild(LockedBody(position=(24,-24), radius=2, color=pg.Color(180,180,240,255) ,speed=-2))
        outerPlanet.addChild (LockedBody(position=(40, 40), radius=5, color=pg.Color(50,255,100,255)  ,speed=-1))
        outerPlanet.addChild (LockedBody(position=(55,-55), radius=4, color=pg.Color(200,40,255,255)  ,speed=-0.8))
        outerPlanet.addChild (LockedBody(position=(30,0)  , radius=7, color=pg.Color(200,200,255,255) ,speed=-3))
        
        # Setup parents
        for body in self.rootBody:
            for child in body.children:
                child.parentBody = body
        
        # Circular paths for all except sun
        for body in self.rootBody:
            if body != self.rootBody:
                body.setPath(CircularPath())
        
    def worldToScreen(self, pos):
        """ Converts a world position to a screen position, requires tuple for x and y """
        return (int(pos[0]) + self.width/2, int(pos[1]) + self.height/2)  
        
    def drawCircle(self, surface, pos, color, radius):
        screenPos = self.worldToScreen(pos)
        pg.draw.circle(surface, color, (screenPos[0], screenPos[1]), radius)
    
    def step(self, dt):
        """ Computes one game step or tick, dt being the 
            approx time elapsed since the previous tick """
         
        black = (0, 0, 0)
        self.screen.fill(black)
        
        self.input.update()
        
        # Iterate over tree, update and draw
        for body in self.rootBody:
            body.update(dt)
            self.drawCircle(self.screen, body.getWorldPosition(), body.color, body.radius)
        
        pg.display.flip()
    
    def gameLoop(self):
        """ Loops until gameOver is set to true. A minimum time between updates
            is enforced, and elapsed time is calculated to an approximate value. """  
        taken = self.minDt
        while not self.gameOver:
            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()
                elif event.type==pg.VIDEORESIZE: self.screenResize(event) 
            start = clock()
            self.step(taken)
            taken = clock() - start
            taken = taken * 1000
            if taken < self.minDt:
                sleep((self.minDt - taken)/1000)
                taken = self.minDt
        sys.exit()
    
    def screenResize(self, data):
        self.width, self.height = data.dict["size"]
        self.screen = pg.display.set_mode((self.width, self.height), 
                      pg.HWSURFACE|pg.DOUBLEBUF|pg.RESIZABLE) 
