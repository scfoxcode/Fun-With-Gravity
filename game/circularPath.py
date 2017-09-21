from path import Path
from vec2D import Vec2D
import math

class CircularPath(Path):
    """ Rotates the position vector to provide a circular path around the origin """
    def updatePosition(self, pos, speed, dt):
        return Vec2D.rotate(pos, speed*0.001*dt)