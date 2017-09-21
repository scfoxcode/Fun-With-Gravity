import sys
import pygame as pg
from userInput import UserInput
from lockedBody import LockedBody
from circularPath import CircularPath
from time import sleep, clock
from vec2D import Vec2D

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
        self.input.gameRef = self
        self.setupSystem()   
    
    def setupSystem(self):   
        """ Defines the bodies in the solar system, initialises the system tree and creates an empty list for dynamic bodies """
        # Create the sun
        self.rootBody  = LockedBody(radius=35, color=pg.Color(255,255,0,255), mass=1.0)
        
        # Create planets
        innerPlanet    = LockedBody(position=Vec2D(-70, 0)  , radius=6 , color=pg.Color(255,128,0,255), speed=-1.5  , mass=0.5)
        middlePlanet   = LockedBody(position=Vec2D(150,0)   , radius=10, color=pg.Color(0,0,255,255)  , speed=-0.5  , mass=0.5)
        outerPlanet    = LockedBody(position=Vec2D(220, 220), radius=18, color=pg.Color(255,70,20,255), speed=-0.15 , mass=0.5)
        self.rootBody.addChild(innerPlanet)
        self.rootBody.addChild(middlePlanet)
        self.rootBody.addChild(outerPlanet)
        
        # Add moons
        middlePlanet.addChild(LockedBody(position=Vec2D(14,14) , radius=5, color=pg.Color(255,255,255,255), speed=-1.5 , mass=0.2))
        middlePlanet.addChild(LockedBody(position=Vec2D(24,-24), radius=2, color=pg.Color(180,180,240,255), speed=-1   , mass=0.2))
        outerPlanet.addChild (LockedBody(position=Vec2D(40, 40), radius=5, color=pg.Color(50,255,100,255) , speed=-0.5 , mass=0.2))
        outerPlanet.addChild (LockedBody(position=Vec2D(55,-55), radius=4, color=pg.Color(200,40,255,255) , speed=-0.4 , mass=0.2))
        outerPlanet.addChild (LockedBody(position=Vec2D(30,0)  , radius=7, color=pg.Color(200,200,255,255), speed=-1.5 , mass=0.2))
        
        # Setup parents
        for body in self.rootBody:
            for child in body.children:
                child.parentBody = body
        
        # Circular paths for all except sun
        for body in self.rootBody:
            if body != self.rootBody:
                body.setPath(CircularPath())
                
        # Create empty list for dynamic bodies
        self.dynamicBodies = []
        
    def addDynamicBody(self, body):
        """ Apends a dynamic body to the dynamic bodies in list.
        Once in the list the object will be updated and drawn """
        self.dynamicBodies.append(body)
                
    def screenToWorld(self, pos):
        """ Converts a screen position to a world position """
        return Vec2D(pos.x - self.width/2, pos.y - self.height/2)  
        
    def worldToScreen(self, pos):
        """ Converts a world position to a screen position """
        return Vec2D(pos.x + self.width/2, pos.y + self.height/2)  
        
    def drawCircle(self, surface, pos, color, radius):
        """ Uses a world position to draw a circle in the world space """
        screenPos = self.worldToScreen(pos)
        pg.draw.circle(surface, color, (int(screenPos.x), int(screenPos.y)), radius)
    
    def step(self, dt):
        """ Computes one game step or tick, dt being the 
            approx time elapsed since the previous tick """
         
        black = (0, 0, 0)
        self.screen.fill(black)
        
        # Handle body drag creation
        self.input.update()
        if self.input.body:
            body   = self.input.body
            clickP = self.input.clickPosition
            pg.draw.line(self.screen, pg.Color(255,255,255,255),
                        (clickP.x, clickP.y), (body.position.x, body.position.y), 1)
            self.drawCircle(self.screen, self.screenToWorld(body.position), 
                            pg.Color(255,255,255,255), body.radius)                 
        
        lockedPhysicsList = [] # Used for dynamic calculations and collisions
        
        # Iterate over tree, update and draw
        for body in self.rootBody:
            body.update(dt)
            bodyPos = body.getWorldPosition()
            self.drawCircle(self.screen, bodyPos, body.color, body.radius)
            lockedPhysicsList.append(body)
            
        # Update and draw all dynamic bodies
        for index, body in enumerate(self.dynamicBodies):
            body.update(lockedPhysicsList, dt)
            self.drawCircle(self.screen, (body.position), 
                            pg.Color(255,255,255,255), body.radius)  
            if Vec2D.magnitudeSquared(body.position) > 1000000: # Out of game area
                del self.dynamicBodies[index]
        
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
        """ Updates the width and height on screen resize """
        self.width, self.height = data.dict["size"]
        self.screen = pg.display.set_mode((self.width, self.height), 
                      pg.HWSURFACE|pg.DOUBLEBUF|pg.RESIZABLE) 