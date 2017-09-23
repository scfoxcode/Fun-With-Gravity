import pygame as pg
import xml.etree.ElementTree
from lockedBody import LockedBody
from vec2D import Vec2D

class Map():
    
    def __init__(self):
        self.root = None
        
    def parseNode(self, parent, node):
        position = node.get("position")
        radius   = node.get("radius")
        speed    = node.get("speed")
        color    = node.get("color")
        mass     = node.get("mass")
        
        if radius:
            radius = int(radius)
        else:
            radius = 10.0
        
        if speed:
            speed = float(speed)
        else:
            speed = 1.0
            
        if mass:
            mass = float(mass)
        else:
            mass = 1.0
            
        if position:
            position = position.split(",")
            position = Vec2D(int(position[0]), int(position[1]))
        else:
            position = Vec2D(0, 0)
        
        if color:
            color = color.split(",")
            color = pg.Color(int(color[0]), int(color[1]), 
                             int(color[2]), int(color[3]))
        else:
            color = pg.Color(255,255,255,255)
        
            
        # Create the node
        body = LockedBody(position = position, 
                          radius   = radius, 
                          color    = color, 
                          mass     = mass,
                          speed    = speed)
        
        if parent:
            body.parentBody = parent
        
        for child in node:
            body.addChild(self.parseNode(body, child))
        
        return body
        
    
    def importMap(self, filename='./maps/default.map'):
        root = xml.etree.ElementTree.parse(filename).getroot()
        self.root = self.parseNode(None, root)
        return self.root
