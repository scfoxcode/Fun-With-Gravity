from vec2D import Vec2D
import math

class DynamicBody():
    """ A dynamic body is used to represent an object that
    is affected by forces in the world. They have no gravity of their own
    but are effected by the mass of LockedBodies """
    
    def __init__(self, position=Vec2D(0,0), velocity=Vec2D(0, 0), radius=3):
        self.gConstant = 2
        self.position  = position
        self.velocity  = velocity
        self.radius    = radius
        self.collided  = False
    
    def update(self, lockedBodies, dt):
        """ Updates velocity and applies to position based on all
        the locked bodies in the system """
        for body in lockedBodies:
            rawDisplace = body.getWorldPosition() - self.position
            direction = Vec2D.normalize(rawDisplace)
            displacementSquared = Vec2D.magnitudeSquared(rawDisplace)
            acceleration = dt*self.gConstant*body.mass/max(10, displacementSquared) # min radius 10 to prevent crazy acceleration
            self.velocity = self.velocity + Vec2D.scale(direction, acceleration)
            self.position = self.position + self.velocity
            
            # Have we collided
            if not self.collided:
                actualDisplacement = math.sqrt(displacementSquared)
                if actualDisplacement < (self.radius + body.radius):
                    self.collided = True # Collision has occured
    
    def hasCollided(self):
        """ returns the collided flag, used to delete object """
        return self.collided
            

        