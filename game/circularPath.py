from path import Path
import math

class CircularPath(Path):
    
    def updatePosition(self, pos, speed, dt):
        sn = math.sin(speed*0.001*dt)
        cs = math.cos(speed*0.001*dt)
        x = pos[0] * cs - pos[1] * sn
        y = pos[0] * sn + pos[1] * cs
        return (x, y)