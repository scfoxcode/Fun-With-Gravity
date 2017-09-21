from path import Path
from vec2D import Vec2D
import math

class CircularPath(Path):
    
    def updatePosition(self, pos, speed, dt):
        sn = math.sin(speed*0.001*dt)
        cs = math.cos(speed*0.001*dt)
        x = pos.x * cs - pos.y * sn
        y = pos.x * sn + pos.y * cs
        return Vec2D(x, y)